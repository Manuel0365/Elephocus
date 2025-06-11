from Model.usuariosModel import UsuarioInsert, Salida, UsuarioSalida, UsuarioSelect
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

class UsuariosDAO:
    def __init__(self, db):
        self.db = db

    def agregarUsuario(self, usuario: UsuarioInsert):
        salida = Salida(estatus="", mensaje="")
        try:
            # Validar que la edad sea mayor o igual a 8
            if usuario.edad < 8:
                salida.estatus = "ERROR"
                salida.mensaje = "La edad debe ser mayor o igual a 8 años."
                return salida

            # Validar que el nivel_academico sea válido
            niveles_validos = ["Primaria", "Secundaria", "Preparatoria", "Universidad", "Libre"]
            if usuario.nivel_academico not in niveles_validos:
                salida.estatus = "ERROR"
                salida.mensaje = f"El nivel académico debe ser uno de los siguientes: {', '.join(niveles_validos)}."
                return salida

            # Verificar si el correo ya existe
            correo_existente = self.db.usuarios.find_one({"correo": usuario.correo})
            if correo_existente:
                salida.estatus = "ERROR"
                salida.mensaje = "El correo ya está registrado. Por favor, usa otro correo."
                return salida

            # Insertar el usuario si las validaciones son correctas
            result = self.db.usuarios.insert_one(jsonable_encoder(usuario))
            salida.estatus = "OK"
            salida.mensaje = "Usuario agregado con éxito con id: " + str(result.inserted_id)
        except Exception as ex:
            print(ex)
            salida.estatus = "ERROR"
            salida.mensaje = "Error al registrar el usuario, consulta al administrador."
        return salida
    
    def eliminarUsuario(self, idUsuario: str) -> dict:
        salida = Salida(estatus="", mensaje="")
        try: 
            resultado = self.db.usuarios.delete_one({"_id": ObjectId(idUsuario)})
            if resultado.deleted_count > 0:
                salida.estatus = "OK"
                salida.mensaje = "Usuario eliminado"
            else:
                print(idUsuario)
                salida.estatus = "ERROR"
                salida.mensaje = "No se encontró el usuario"
        except Exception as ex:
            print("Error en eliminar usuario:", ex)
            salida.estatus = "ERROR"
            salida.mensaje = "Error al eliminar al usuario"
        return salida
    
    def actualizarUsuario(self, idUsuario: str, datos: dict) -> dict:
        salida = Salida(estatus="", mensaje="")
        try:
            if not ObjectId.is_valid(idUsuario):
                salida.estatus = "ERROR"
                salida.mensaje = "ID inválido"
                return salida.dict()

            resultado = self.db.usuarios.update_one(
                {"_id": ObjectId(idUsuario)},
                {"$set": datos}
            )

            if resultado.modified_count > 0:
                salida.estatus = "OK"
                salida.mensaje = "Usuario actualizado"
            elif resultado.matched_count > 0:
                salida.estatus = "OK"
                salida.mensaje = "Usuario ya estaba con esos datos"
            else:
                salida.estatus = "ERROR"
                salida.mensaje = "No se encontró el usuario"
        except Exception as ex:
            print("Error en actualizar usuario:", ex)
            salida.estatus = "ERROR"
            salida.mensaje = "Error al actualizar al usuario"

        return salida

    def consultarUsuario(self, idUsuario: str) -> dict:
            salida = Salida(estatus="", mensaje="")
            try:
                if not ObjectId.is_valid(idUsuario):
                    salida.estatus = "ERROR"
                    salida.mensaje = "ID inválido"
                    return salida.dict()

                resultado = self.db.usuariosView.find_one({"_id": ObjectId(idUsuario)})
                if resultado:
                    usuario = UsuarioSelect(**resultado)
                    return usuario.dict()
                else:
                    salida.estatus = "ERROR"
                    salida.mensaje = "No se encontró el usuario"
            except Exception as ex:
                print("Error en consultar usuario:", ex)
                salida.estatus = "ERROR"
                salida.mensaje = "Error al consultar al usuario"
            return salida


    def consultaGeneral(self):
        from Model.usuariosModel import UsuarioSelect
        salida = UsuarioSalida(estatus="", mensaje="", usuarios=[])
        try:
            lista = list(self.db.usuariosView.find())
            salida.estatus = "OK"
            salida.mensaje = "Listado de usuarios"
            salida.usuarios = [
                UsuarioSelect(**{**usuario, "_id": str(usuario["_id"])})
                for usuario in lista
            ]
        except Exception as e:
            salida.estatus = "ERROR"
            salida.mensaje = f"Error al consultar los usuarios: {str(e)}"
            salida.usuarios = []
        return salida
    
    def autenticar(self, correo, password):
        respuesta = UsuarioSalida(estatus="", mensaje="", usuarios=None)
        try:
            usuarios = self.db.usuarios.find_one(
                {"correo": correo, "password": password, "estatus": "A"},
                projection={"tarjetas": False}
            )
            if usuarios:
                usuarios["_id"] = str(usuarios["_id"])  
                usuario_data = UsuarioSelect(**usuarios)
                respuesta.estatus = "OK"
                respuesta.mensaje = "Usuario autenticado con éxito"
                respuesta.usuarios = usuario_data
            else:
                respuesta.estatus = "ERROR"
                respuesta.mensaje = "Datos incorrectos"
        except Exception as ex:
            print("Error en autenticar:", ex)
            respuesta.estatus = "ERROR"
            respuesta.mensaje = "Error interno al autenticar el usuario, consulta al administrador"
        return respuesta

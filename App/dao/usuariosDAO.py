from Model.usuariosModel import UsuarioInsert, Salida, UsuarioSalida, UsuarioSelect
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

class UsuariosDAO:
    def __init__(self, db):
        self.db = db

    def agregarUsuario(self, usuario: UsuarioInsert):
        salida = Salida(estatus="", mensaje="")
        try:
            result = self.db.usuarios.insert_one(jsonable_encoder(usuario))
            salida.estatus = "OK"
            salida.mensaje = "Usuario agregado con exito con id: " + str(result.inserted_id)
        except Exception as ex:
            print(ex)
            salida.estatus = "ERROR"
            salida.mensaje = "Error al registrar el usuario, consulta al adminstrador."
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
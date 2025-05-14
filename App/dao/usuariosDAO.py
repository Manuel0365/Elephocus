from Model.usuariosModel import UsuarioInsert, Salida
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


from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from Model.usuariosModel import UsuarioInsert, Salida

class UsuariosDAO:
    def __init__(self, db):
        self.db = db

    def agregar(self, usuario: UsuarioInsert) -> dict:
        salida = Salida(estatus="", mensaje="")
        try:
            doc = jsonable_encoder(usuario)
            result = self.db.flashcards.insert_one(doc)
            salida.estatus = "OK"
            salida.mensaje = "Flashcard Creada con éxito"
        except Exception as ex:
            print("Error en agregar flashcard:", ex)
            salida.estatus = "ERROR"
            salida.mensaje = "Error al crear la flashcard"
        return salida.dict()

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


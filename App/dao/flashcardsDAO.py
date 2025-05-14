from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from .flashcardsModel import FlashcardInsert, Salida

class FlashcardsDAO:
    def __init__(self, db):
        self.db = db

    def agregar(self, flashcard: FlashcardInsert) -> dict:
        salida = Salida(estatus="", mensaje="")
        try:
            doc = jsonable_encoder(flashcard)
            result = self.db.flashcards.insert_one(doc)
            salida.estatus = "OK"
            salida.mensaje = str(result.inserted_id)
        except Exception:
            salida.estatus = "ERROR"
            salida.mensaje = "Error al crear la flashcard"
        return salida.dict()

    def eliminar(self, id_flashcard: str) -> dict:
        salida = Salida(estatus="", mensaje="")
        try:
            obj = self.db.flashcards.find_one({"_id": ObjectId(id_flashcard)})
            if obj:
                self.db.flashcards.delete_one({"_id": ObjectId(id_flashcard)})
                salida.estatus = "OK"
                salida.mensaje = "Flashcard eliminada correctamente"
            else:
                salida.estatus = "ERROR"
                salida.mensaje = "Flashcard no existe"
        except Exception:
            salida.estatus = "ERROR"
            salida.mensaje = "Error al eliminar la flashcard"
        return salida.dict()
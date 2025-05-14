from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from Model.flashcardModel import FlashcardInsert, FlashcardUpdate, Salida, FlashcardResponse

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
        except Exception as ex:
            print("Error en agregar flashcard:", ex)
            salida.estatus = "ERROR"
            salida.mensaje = "Error al crear la flashcard"
        return salida.dict()

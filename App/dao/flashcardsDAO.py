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
            salida.mensaje = "Flashcard Creada con éxito"
        except Exception as ex:
            print("Error en agregar flashcard:", ex)
            salida.estatus = "ERROR"
            salida.mensaje = "Error al crear la flashcard"
        return salida.dict()

    def eliminar(self, id_flashcard: str) -> dict:
        salida = Salida(estatus="", mensaje="")
        try:
            oid = ObjectId(id_flashcard)
            result = self.db.flashcards.delete_one({"_id": oid})
            if result.deleted_count == 1:
                salida.estatus = "OK"
                salida.mensaje = "Flashcard eliminada correctamente"
            else:
                salida.estatus = "ERROR"
                salida.mensaje = "Flashcard no existe"
        except Exception as ex:
            print("Error en eliminar flashcard:", ex)
            salida.estatus = "ERROR"
            salida.mensaje = "Error al eliminar la flashcard"
        return salida.dict()

    def actualizar(self, id_flashcard: str, data: FlashcardUpdate) -> dict:
        try:
            oid = ObjectId(id_flashcard)
        except Exception:
            return {"mensaje": "ID de flashcard inválido"}

        update_data = jsonable_encoder(data)
        result = self.db.flashcards.update_one(
            {"_id": oid},
            {"$set": update_data}
        )
        if result.matched_count == 0:
            return {"mensaje": "Flashcard no existe"}

        doc = self.db.flashcards.find_one({"_id": oid})
        return FlashcardResponse(
            mensaje="Flashcard actualizada correctamente",
            _id=str(doc['_id']),
            pregunta=doc['pregunta'],
            respuesta=doc['respuesta']
        ).dict()

    def consultaGeneral(self) -> list:
        flashcards = []
        try:
            docs = self.db.flashcards.find()
            for doc in docs:
                flashcards.append({
                    "_id": str(doc.get("_id", "")),
                    "pregunta": doc.get("pregunta", ""),
                    "respuesta": doc.get("respuesta", ""),
                    "id_temario": str(doc.get("id_tema", "")),
                    "autor": str(doc.get("autor", "")),
                    "fecha_creacion": doc.get("fecha_creacion", "").isoformat() if isinstance(doc.get("fecha_creacion"), datetime) else ""
                })
        except Exception as ex:
            print("Error en consulta general:", ex)
        return flashcards

    def consultaPorId(self, id_flashcard: str) -> dict:
            try:
                oid = ObjectId(id_flashcard)
            except Exception:
                return {"mensaje": "ID de flashcard inválido"}
    
            doc = self.db.flashcards.find_one({"_id": oid})
            if doc:
                return {
                    "_id": str(doc["_id"]),
                    "id_temario": str(doc["id_tema"]),
                    "pregunta": doc["pregunta"],
                    "respuesta": doc["respuesta"]
                }
            return {"mensaje": "La flashcard no existe"}

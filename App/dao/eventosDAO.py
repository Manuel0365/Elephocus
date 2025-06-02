from bson import ObjectId
from Model.eventoModel import EventoInsert, EventoUpdate, Evento
from fastapi.encoders import jsonable_encoder

class EventosDAO:
    def __init__(self, db):
        self.collection = db["eventos"]

    def agregar(self, evento_data: EventoInsert, autor: str):
        evento_dict = jsonable_encoder(evento_data)
        evento_dict["autor"] = autor
        result = self.collection.insert_one(evento_dict)
        return {
            "estatus": "OK",
            "mensaje": "Evento creado exitosamente",
            "id": str(result.inserted_id)
        }

    def actualizar(self, id_evento: str, evento_data: EventoUpdate):
        result = self.collection.update_one(
            {"_id": ObjectId(id_evento)},
            {"$set": {k: v for k, v in evento_data.dict().items() if v is not None}}
        )
        if result.matched_count == 0:
            return {"estatus": "ERROR", "mensaje": "Evento no encontrado"}

        evento_actualizado = self.collection.find_one({"_id": ObjectId(id_evento)})
        evento_actualizado["_id"] = str(evento_actualizado["_id"])
        return {"estatus": "OK", "evento": Evento(**evento_actualizado)}

    def eliminar(self, id_evento: str):
        result = self.collection.delete_one({"_id": ObjectId(id_evento)})
        if result.deleted_count == 0:
            return {"estatus": "ERROR", "mensaje": "Evento no encontrado"}
        return {"estatus": "OK", "mensaje": "Evento eliminado correctamente"}

    def consultaGeneral(self):
        eventos = list(self.collection.find())
        for evento in eventos:
            evento["_id"] = str(evento["_id"])
        return [Evento(**evento) for evento in eventos]

    def consultaPorId(self, id_evento: str):
        evento = self.collection.find_one({"_id": ObjectId(id_evento)})
        if not evento:
            return {"estatus": "ERROR", "mensaje": "El evento no existe"}
        evento["_id"] = str(evento["_id"])
        return Evento(**evento)

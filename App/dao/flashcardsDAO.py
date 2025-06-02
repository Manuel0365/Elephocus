from bson import ObjectId
# Asegúrate de que Flashcard esté importado desde tu flashcardModel.py
from Model.flashcardModel import FlashcardInsert, FlashcardUpdate, Salida, FlashcardResponse, Flashcard
from datetime import datetime


class FlashcardsDAO:
    def __init__(self, db):
        self.db = db

    def agregar(self, flashcard_data: FlashcardInsert, autor_id: str) -> dict:
        
        salida = Salida(estatus="", mensaje="")
        try:
            doc = flashcard_data.model_dump()  
            doc['autor'] = autor_id
            doc['fecha_creacion'] = datetime.now()

            if 'id_temario' in doc and 'id_tema' not in doc:
                doc['id_tema'] = doc.pop('id_temario')

            result = self.db.flashcards.insert_one(doc)
            if result.inserted_id:
                salida.estatus = "OK"
                salida.mensaje = f"Flashcard Creada con éxito con ID: {str(result.inserted_id)}"
            else:
                salida.estatus = "ERROR"
                salida.mensaje = "No se pudo crear la flashcard"
        except Exception as ex:
            print(f"Error en agregar flashcard: {ex}")
            salida.estatus = "ERROR"
            salida.mensaje = "Error al crear la flashcard"
        return salida.model_dump()  

    def consultaPorId(self, id_flashcard: str) -> Flashcard | dict:
        
        try:
            oid = ObjectId(id_flashcard)
        except Exception:
            return {"mensaje": "ID de flashcard inválido"}

        doc = self.db.flashcards.find_one({"_id": oid})
        if doc:
            
            fecha_creacion_doc = doc.get("fecha_creacion")
            if isinstance(fecha_creacion_doc, str):
                try:
                    fecha_creacion_doc = datetime.fromisoformat(fecha_creacion_doc)
                except ValueError:
                    fecha_creacion_doc = datetime.min  
            elif not isinstance(fecha_creacion_doc, datetime):
                fecha_creacion_doc = datetime.min

            id_tema_doc = str(doc.get("id_tema", doc.get("id_temario", "")))  

            flashcard_model_data = {
                "pregunta": doc.get("pregunta", ""),
                "respuesta": doc.get("respuesta", ""),
                "id_tema": id_tema_doc,
                "autor": doc.get("autor", ""), 
                "fecha_creacion": fecha_creacion_doc
            }

            if not flashcard_model_data["autor"]:
                print(f"Advertencia: Flashcard con ID {id_flashcard} no tiene autor o el campo está vacío.")

            return Flashcard(**flashcard_model_data)

        return {"mensaje": "La flashcard no existe"}

    def actualizar(self, id_flashcard: str, data: FlashcardUpdate) -> dict:
        try:
            oid = ObjectId(id_flashcard)
        except Exception:
            return {"estatus": "ERROR", "mensaje": "ID de flashcard inválido"}

        update_data = data.model_dump(exclude_unset=True)

        if not update_data: 
            doc_existente = self.db.flashcards.find_one({"_id": oid})
            if not doc_existente:
                return {"estatus": "ERROR", "mensaje": "Flashcard no existe"}
            return FlashcardResponse(
                mensaje="No se proporcionaron datos para actualizar.",
                _id=str(doc_existente['_id']),
                pregunta=doc_existente['pregunta'],
                respuesta=doc_existente['respuesta']
            ).model_dump()

        result = self.db.flashcards.update_one(
            {"_id": oid},
            {"$set": update_data}
        )

        if result.matched_count == 0:
            return {"estatus": "ERROR", "mensaje": "Flashcard no existe"}

        doc_actualizado = self.db.flashcards.find_one({"_id": oid})
        if not doc_actualizado: 
            return {"estatus": "ERROR", "mensaje": "Error al recuperar la flashcard después de la actualización."}

        mensaje_respuesta = "Flashcard actualizada correctamente"
        if result.modified_count == 0:
            mensaje_respuesta = "La flashcard ya contenía estos datos."

        return FlashcardResponse(
            mensaje=mensaje_respuesta,
            _id=str(doc_actualizado['_id']),
            pregunta=doc_actualizado['pregunta'],
            respuesta=doc_actualizado['respuesta']
        ).model_dump()

    def eliminar(self, id_flashcard: str) -> dict:
        
        salida = Salida(estatus="", mensaje="")
        try:
            oid = ObjectId(id_flashcard)  #
            result = self.db.flashcards.delete_one({"_id": oid})  #
            if result.deleted_count == 1:  #
                salida.estatus = "OK"
                salida.mensaje = "Flashcard eliminada correctamente"  #
            else:
                salida.estatus = "ERROR"  
                salida.mensaje = "Flashcard no existe"  #
        except Exception as ex:
            print(f"Error en eliminar flashcard: {ex}")
            salida.estatus = "ERROR"
            salida.mensaje = "Error al eliminar la flashcard"  #
        return salida.model_dump()

    def consultaGeneral(self) -> list[Flashcard]:
        
        flashcards_list = []
        try:
            docs = self.db.flashcards.find()  #
            for doc in docs:
                fecha_creacion_doc = doc.get("fecha_creacion")
                if isinstance(fecha_creacion_doc, str):
                    try:
                        fecha_creacion_doc = datetime.fromisoformat(fecha_creacion_doc)
                    except ValueError:
                        fecha_creacion_doc = datetime.min
                elif not isinstance(fecha_creacion_doc, datetime):
                    fecha_creacion_doc = datetime.min

                id_tema_doc = str(doc.get("id_tema", doc.get("id_temario", "")))

                flashcard_model_data = {
                    "pregunta": doc.get("pregunta", ""),  
                    "respuesta": doc.get("respuesta", ""),  
                    "id_tema": id_tema_doc,  
                    "autor": doc.get("autor", ""),  
                    "fecha_creacion": fecha_creacion_doc  
                }
                flashcards_list.append(Flashcard(**flashcard_model_data))
        except Exception as ex:
            print(f"Error en consulta general de flashcards: {ex}")
        return flashcards_list
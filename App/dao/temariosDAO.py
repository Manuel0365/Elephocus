from Model.temariosModel import TemarioInsert, Salida, TemarioSelect, TemarioSalida
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

class TemariosDAO:
    def __init__(self, db):
        self.db = db

    # Agregar un temario
    def agregarTemario(self, temario: TemarioSelect):
        salida = Salida(estatus="", mensaje="")
        try:
            result = self.db.temas.insert_one(jsonable_encoder(temario))
            salida.estatus = "OK"
            salida.mensaje = "Temario agregado con éxito con id: " + str(result.inserted_id)
        except Exception as ex:
            print(ex)
            salida.estatus = "ERROR"
            salida.mensaje = "Error al registrar el temario, consulta al adminstrador."
        return salida

    # Consultar un temario por ID
    def consultarTemario(self, idTemario: str) -> dict:
            salida = Salida(estatus="", mensaje="")
            try:
                if not ObjectId.is_valid(idTemario):
                    salida.estatus = "ERROR"
                    salida.mensaje = "ID inválido"
                    return salida.dict()

                resultado = self.db.temasView.find_one({"_id": ObjectId(idTemario)})
                if resultado:
                    temario = TemarioSelect(**resultado)
                    return temario.dict()
                else:
                    salida.estatus = "ERROR"
                    salida.mensaje = "No se encontró el temario."
            except Exception as ex:
                print("Error en consultar el temario:", ex)
                salida.estatus = "ERROR"
                salida.mensaje = "Error al consultar el temario"
            return salida

    def consultaGeneral(self):
        salida = TemarioSalida(estatus="", mensaje="", temarios=[])
        try:
            lista = list(self.db.temasView.find())
            salida.estatus = "OK"
            salida.mensaje = "Listado de temarios"
            salida.temarios = [
                TemarioSelect(**{**temario, "_id": str(temario["_id"])})
                for temario in lista
            ]
        except Exception as e:
            salida.estatus = "ERROR"
            salida.mensaje = f"Error al consultar los temarios: {str(e)}"
            salida.temarios = []
        return salida
    
    # Eliminar un temario
    def eliminarTemario(self, idTemario) -> dict:
        salida = Salida(estatus="", mensaje="")
        try:
            resultado = self.db.temas.delete_one({"_id": ObjectId(idTemario)})
            if resultado.deleted_count > 0:
                salida.estatus = "OK"
                salida.mensaje = "Temario eliminado con éxito."
            else:
                print(idTemario)
                salida.estatus = "ERROR"
                salida.mensaje = "No se encontró el temario con el id proporcionado."
        except Exception as ex:
            print(ex)
            salida.estatus = "ERROR"
            salida.mensaje = "Error al eliminar el temario, consulta al administrador."
        return salida

    # Actualizar un temario
    def actualizarTemario(self, idTemario: str, datos: dict) -> dict:
        salida = Salida(estatus="", mensaje="")
        try:
            if not ObjectId.is_valid(idTemario):
                salida.estatus = "ERROR"
                salida.mensaje = "ID inválido"
                return salida.dict()

            resultado = self.db.temas.update_one(
                {"_id": ObjectId(idTemario)},
                {"$set": datos}
            )

            if resultado.modified_count > 0:
                salida.estatus = "OK"
                salida.mensaje = "Temario actualizado con éxito."
            elif resultado.matched_count > 0:
                salida.estatus = "OK"
                salida.mensaje = "El temario ya estaba con esos datos."
            else:
                salida.estatus = "ERROR"
                salida.mensaje = "No se encontró el temario con el id proporcionado."
        except Exception as ex:
            print("Error al actualizar el temario:", ex)
            salida.estatus = "ERROR"
            salida.mensaje = "Error al actualizar el temario, consulta al administrador."
        return salida
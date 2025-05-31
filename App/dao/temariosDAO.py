from Model.temariosModel import TemarioInsert, Salida
from fastapi.encoders import jsonable_encoder

class TemariosDAO:
    def __init__(self, db):
        self.db = db

    def agregarTemario(self, temario):
        salida = {"estatus": "", "mensaje": ""}
        try:
            result = self.db.temas.insert_one(jsonable_encoder(temario))
            salida["estatus"] = "OK"
            salida["mensaje"] = "Temario agregado con éxito con id: " + str(result.inserted_id)
        except Exception as ex:
            print(ex)
            salida["estatus"] = "ERROR"
            salida["mensaje"] = "Error al registrar el temario, consulta al administrador."
        return salida
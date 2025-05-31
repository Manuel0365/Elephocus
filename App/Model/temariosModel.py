# Modificar
from pydantic import BaseModel

class TemarioInsert(BaseModel):
    nombre: str
    descripcion: str

class Salida(BaseModel):
    estatus: str
    mensaje: str
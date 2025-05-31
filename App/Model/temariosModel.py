from typing import Optional, List
from pydantic import BaseModel

class TemarioInsert(BaseModel):
    nombre: str
    descripcion: str

class Salida(BaseModel):
    estatus: str
    mensaje: str

class TemarioUpdate(BaseModel):
    nombre: Optional[str]
    descripcion: Optional[str]
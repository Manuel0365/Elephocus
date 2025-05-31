from typing import Optional, List
from pydantic import BaseModel, Field

class TemarioInsert(BaseModel):
    nombre: str
    descripcion: str

class TemarioSelect(BaseModel):
    _id: str
    nombre: str
    descripcion: str

class Salida(BaseModel):
    estatus: str
    mensaje: str

class TemarioUpdate(BaseModel):
    nombre: Optional[str]
    descripcion: Optional[str]

class TemarioSalida(Salida):
    temarios: List[TemarioSelect] = Field(default_factory=list)
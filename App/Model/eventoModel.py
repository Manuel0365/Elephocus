from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId

class EventoInsert(BaseModel):
    nombre: str
    fecha: datetime

class EventoUpdate(BaseModel):
    nombre: Optional[str] = None
    fecha: Optional[datetime] = None

class Evento(BaseModel):
    id: str = Field(alias="_id")
    nombre: str
    fecha: datetime
    autor: str

class Salida(BaseModel):
    estatus: str
    mensaje: str

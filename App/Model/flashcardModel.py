from datetime import datetime
from pydantic import BaseModel

class FlashcardInsert(BaseModel):
    id_temario: str
    pregunta: str
    respuesta: str

class FlashcardUpdate(BaseModel):
    pregunta: str
    respuesta: str

class Flashcard(BaseModel):
    pregunta: str
    respuesta: str
    id_tema: str
    autor: str
    fecha_creacion: datetime

class Salida(BaseModel):
    estatus: str
    mensaje: str

class FlashcardResponse(BaseModel):
    mensaje: str
    _id: str
    pregunta: str
    respuesta: str
from pydantic import BaseModel

class FlashcardInsert(BaseModel):
    id_temario: str
    pregunta: str
    respuesta: str

class Flashcard(BaseModel):
    _id: str
    id_temario: str
    pregunta: str
    respuesta: str

class Salida(BaseModel):
    estatus: str
    mensaje: str
from pydantic import BaseModel

class UsuarioInsert(BaseModel):
    _id: str
    nombre: str
    email: str
    password: str
    edad: int
    grado: str 

class Salida(BaseModel):
    estatus: str
    mensaje: str

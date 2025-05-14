from pydantic import BaseModel

class UsuarioInsert(BaseModel):
    nombre: str
    correo: str
    password: str
    edad: int
    nivel_academico: str
    pais_region: str 
    estatus: str
    tipo_usuario: str

class Salida(BaseModel):
    estatus: str
    mensaje: str

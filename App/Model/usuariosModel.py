from pydantic import BaseModel
from typing import Optional

class UsuarioInsert(BaseModel):
    nombre: str
    correo: str
    password: str
    edad: int
    nivel_academico: str
    pais_region: str 
    estatus: str
    tipo_usuario: str

class UsuarioSelect(BaseModel):
    _id: str
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

class UsuarioUpdate(BaseModel):
    _id: str
    nombre: Optional[str]
    correo: Optional[str]
    password: Optional[str]
    edad: Optional[int]
    nivel_academico: Optional[str] 
    pais_region: Optional[str] 
    estatus: Optional[str] 
    tipo_usuario: Optional[str] 

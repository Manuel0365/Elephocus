from dao.usuariosDAO import UsuariosDAO
from fastapi import APIRouter, Request
from Model.usuariosModel import UsuarioInsert, Salida

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

@router.post("/crearUsuario", response_model=Salida)
async def crearUsuario(usuario: UsuarioInsert, request: Request)->Salida:
    usuarioDAO = UsuariosDAO(request.app.db)
    return usuarioDAO.agregarUsuario(usuario)

# Eliminar un usuarios
@router.delete("/eliminarUsuario/{idUsuario}", response_model=Salida)
async def eliminarUsuario(idUsuario: str, request: Request) -> Salida:
    usuarioDAO = UsuariosDAO(request.app.db)
    return usuarioDAO.eliminarUsuario(idUsuario)

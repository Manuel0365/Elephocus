from dao.usuariosDAO import UsuariosDAO
from fastapi import APIRouter, Request
from Model.usuariosModel import UsuarioInsert, Salida, UsuarioUpdate

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

#Crear un usuario
@router.post("/crearUsuario", response_model=Salida)
async def agregarUsuario(usuario: UsuarioInsert, request: Request) -> Salida:
    usuarioDAO = UsuariosDAO(request.app.db)
    return usuarioDAO.agregarUsuario(usuario)

# Eliminar un usuario
@router.delete("/eliminarUsuario/{idUsuario}", response_model=Salida)
async def eliminarUsuario(idUsuario: str, request: Request) -> Salida:
    usuarioDAO = UsuariosDAO(request.app.db)
    return usuarioDAO.eliminarUsuario(idUsuario)

# Actualizar un usuario
@router.put("/actualizarUsuario/{idUsuario}", response_model=Salida)
async def actualizarUsuario(idUsuario: str, datos: UsuarioUpdate, request: Request) -> Salida:
    usuarioDAO = UsuariosDAO(request.app.db)
    return usuarioDAO.actualizarUsuario(idUsuario, datos.dict(exclude_unset=True))
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
<<<<<<< HEAD
    return usuarioDAO.eliminarUsuario(idUsuario)
=======
    return usuarioDAO.eliminarUsuario(idUsuario)

# Actualizar un usuario
@router.put("/actualizarUsuario/{idUsuario}", response_model=Salida)
async def actualizarUsuario(idUsuario: str, datos: UsuarioUpdate, request: Request) -> Salida:
    usuarioDAO = UsuariosDAO(request.app.db)
    return usuarioDAO.actualizarUsuario(idUsuario, datos.dict(exclude_unset=True))
>>>>>>> 82130f37e2ea2a8b870a23953e79584f8a634402

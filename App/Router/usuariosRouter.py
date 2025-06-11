from ctypes.wintypes import HHOOK

from typing import Any
from dao.usuariosDAO import UsuariosDAO
from fastapi import APIRouter, Request, Depends
from Model.usuariosModel import UsuarioInsert, Salida, UsuarioSelect, UsuarioUpdate, UsuarioSalida, Login
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from auth.auth import require_roles, get_current_user


router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

security = HTTPBasic()

@router.post("/Autenticar", response_model=UsuarioSalida, summary="Autenticar un usuario")
async def login(login: Login, request: Request) -> UsuarioSalida:
    usuarioDAO = UsuariosDAO(request.app.db)
    return usuarioDAO.autenticar(login.correo, login.password)


async def validarUsuario(request:Request, credenciales: HTTPBasicCredentials=Depends(security))-> UsuarioSalida:
    usuarioDAO = UsuariosDAO(request.app.db)
    return usuarioDAO.autenticar(credenciales.username, credenciales.password)

#Crear un usuario
@router.post("/crearUsuario", response_model=Salida)
async def agregarUsuario(
    usuario: UsuarioInsert,
    request: Request
) -> Salida:
    usuarioDAO = UsuariosDAO(request.app.db)
    return usuarioDAO.agregarUsuario(usuario)

# Eliminar un usuario
@router.delete("/eliminarUsuario/{idUsuario}", response_model=Salida)
async def eliminarUsuario(
    idUsuario: str,
    request: Request,
    current_user: UsuarioSelect = Depends(require_roles("Admin"))
) -> Salida:
    usuarioDAO = UsuariosDAO(request.app.db)
    return usuarioDAO.eliminarUsuario(idUsuario)

# Actualizar un usuario
@router.put("/actualizarUsuario/{idUsuario}", response_model=Salida)
async def actualizarUsuario(
    idUsuario: str,
    datos: UsuarioUpdate,
    request: Request,
    current_user: UsuarioSelect = Depends(get_current_user)
) -> Salida:
    if current_user.tipo_usuario != "Admin" and current_user._id != idUsuario:
        raise HTTPException(status_code=403, detail="No puedes modificar otro usuario")

    usuarioDAO = UsuariosDAO(request.app.db)
    return usuarioDAO.actualizarUsuario(idUsuario, datos.dict(exclude_unset=True))


# Consultar usuario por su id
@router.get("/consultarUsuario/{idUsuario}", response_model=UsuarioSelect)
async def consultarUsuario(
    idUsuario: str,
    request: Request,
    current_user: UsuarioSelect = Depends(get_current_user)
) -> UsuarioSelect:
    usuarioDAO = UsuariosDAO(request.app.db)
    return usuarioDAO.consultarUsuario(idUsuario)


# Consultar todos los usuarios
@router.get("/", response_model=UsuarioSalida)
async def consultaGeneral(
    request: Request,
    current_user: UsuarioSelect = Depends(require_roles("Admin"))
):
    return UsuariosDAO(request.app.db).consultaGeneral()

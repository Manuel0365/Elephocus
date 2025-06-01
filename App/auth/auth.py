from fastapi import Depends, HTTPException, status, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from bson import ObjectId
from Model.usuariosModel import UsuarioSelect
from dao.usuariosDAO import UsuariosDAO

security = HTTPBasic()

async def get_current_user(request: Request, credentials: HTTPBasicCredentials = Depends(security)) -> UsuarioSelect:
    usuarioDAO = UsuariosDAO(request.app.db)
    resultado = usuarioDAO.autenticar(credentials.username, credentials.password)

    if resultado.estatus != "OK" or not resultado.usuarios:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas o usuario inactivo.",
            headers={"WWW-Authenticate": "Basic"},
        )
    
    return resultado.usuarios


def require_roles(*roles):
    async def role_checker(
        usuario: UsuarioSelect = Depends(get_current_user)
    ):
        if usuario.tipo_usuario not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tienes permisos para acceder a este recurso."
            )
        return usuario
    return role_checker

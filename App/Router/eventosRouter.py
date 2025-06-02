from fastapi import APIRouter, HTTPException, Request, Depends, status
from bson import ObjectId
from Model.eventoModel import EventoInsert, EventoUpdate, Evento, Salida
from Model.usuariosModel import UsuarioSelect
from dao.eventosDAO import EventosDAO
from auth.auth import get_current_user

router = APIRouter(
    prefix="/eventos",
    tags=["Eventos"]
)

@router.post("/crear", response_model=Salida)
async def crear_evento(
        evento_data: EventoInsert,
        request: Request,
        current_user: UsuarioSelect = Depends(get_current_user)
):
    dao = EventosDAO(request.app.db)
    return dao.agregar(evento_data, autor=current_user._id)


@router.put("/{id_evento}", response_model=Evento)
async def actualizar_evento(
        id_evento: str,
        update_data: EventoUpdate,
        request: Request,
        current_user: UsuarioSelect = Depends(get_current_user)
):
    try:
        ObjectId(id_evento)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID de evento inválido")

    dao = EventosDAO(request.app.db)
    evento_obj = dao.consultaPorId(id_evento)

    if isinstance(evento_obj, dict):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=evento_obj.get("mensaje"))

    if current_user.tipo_usuario != "Admin" and evento_obj.autor != current_user._id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permiso para actualizar este evento.")

    resultado = dao.actualizar(id_evento, update_data)

    if resultado.get("estatus") == "ERROR":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=resultado.get("mensaje"))

    return resultado.get("evento")


@router.delete("/{id_evento}", response_model=Salida)
async def eliminar_evento(
        id_evento: str,
        request: Request,
        current_user: UsuarioSelect = Depends(get_current_user)
):
    try:
        ObjectId(id_evento)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID de evento inválido")

    dao = EventosDAO(request.app.db)
    evento_obj = dao.consultaPorId(id_evento)

    if isinstance(evento_obj, dict):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=evento_obj.get("mensaje"))

    if current_user.tipo_usuario != "Admin" and evento_obj.autor != current_user._id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permiso para eliminar este evento.")

    resultado = dao.eliminar(id_evento)

    if resultado.get("estatus") == "ERROR":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=resultado.get("mensaje"))

    return resultado


@router.get("/", response_model=list[Evento])
async def obtener_eventos(
        request: Request,
        current_user: UsuarioSelect = Depends(get_current_user)
):
    if current_user.tipo_usuario != "Admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Solo el administrador puede consultar todos los eventos.")

    dao = EventosDAO(request.app.db)
    return dao.consultaGeneral()


@router.get("/{id_evento}", response_model=Evento)
async def obtener_evento_por_id(
        id_evento: str,
        request: Request,
        current_user: UsuarioSelect = Depends(get_current_user)
):
    try:
        ObjectId(id_evento)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID de evento inválido")

    dao = EventosDAO(request.app.db)
    evento_obj = dao.consultaPorId(id_evento)

    if isinstance(evento_obj, dict):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=evento_obj.get("mensaje"))

    if current_user.tipo_usuario != "Admin" and evento_obj.autor != current_user._id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permiso para ver este evento.")

    return evento_obj

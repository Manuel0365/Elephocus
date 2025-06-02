# flashcardsRouter.py
from fastapi import APIRouter, HTTPException, Request, Depends, status
from Model.flashcardModel import FlashcardInsert, FlashcardUpdate, Salida, FlashcardResponse, Flashcard
from Model.usuariosModel import UsuarioSelect  
from auth.auth import get_current_user  
from dao.flashcardsDAO import FlashcardsDAO  
from bson import ObjectId

router = APIRouter(
    prefix="/flashcards",
    tags=["Flashcards"]
)  

@router.post("/crear", response_model=Salida)  
async def crear_flashcard(
        flashcard_data: FlashcardInsert,
        request: Request,
        current_user: UsuarioSelect = Depends(get_current_user)  
):
    dao = FlashcardsDAO(request.app.db) 
    return dao.agregar(flashcard_data, current_user._id)


@router.put("/{id_flashcard}", response_model=FlashcardResponse)  
async def actualizar_flashcard(
        id_flashcard: str,
        update_data: FlashcardUpdate,  
        request: Request,
        current_user: UsuarioSelect = Depends(get_current_user)  
):
    try:
        ObjectId(id_flashcard)  
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID de flashcard inválido")  #

    dao = FlashcardsDAO(request.app.db)  
    flashcard_obj = dao.consultaPorId(id_flashcard)

    if isinstance(flashcard_obj, dict):  
        error_message = flashcard_obj.get("mensaje", "Error desconocido del DAO")
        status_code_error = status.HTTP_404_NOT_FOUND if "no existe" in error_message.lower() else status.HTTP_400_BAD_REQUEST
        raise HTTPException(status_code=status_code_error, detail=error_message)

    if not isinstance(flashcard_obj, Flashcard): 
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="No se pudo recuperar la flashcard correctamente.")

    if current_user.tipo_usuario != "Admin" and flashcard_obj.autor != current_user._id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para actualizar esta flashcard."
        )

    result_update_dict = dao.actualizar(id_flashcard, update_data)  

    if result_update_dict.get("estatus") == "ERROR":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=result_update_dict.get("mensaje", "Error al actualizar la flashcard"))

    return FlashcardResponse(**result_update_dict)


@router.delete("/{id_flashcard}", response_model=Salida)  
async def eliminar_flashcard(
        id_flashcard: str,
        request: Request,
        current_user: UsuarioSelect = Depends(get_current_user)  
):
    try:
        ObjectId(id_flashcard)  
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID de flashcard inválido")  

    dao = FlashcardsDAO(request.app.db)  
    flashcard_obj = dao.consultaPorId(id_flashcard)

    if isinstance(flashcard_obj, dict):  
        error_message = flashcard_obj.get("mensaje", "Error desconocido del DAO")
        status_code_error = status.HTTP_404_NOT_FOUND if "no existe" in error_message.lower() else status.HTTP_400_BAD_REQUEST
        raise HTTPException(status_code=status_code_error, detail=error_message)

    if not isinstance(flashcard_obj, Flashcard):  
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="No se pudo recuperar la flashcard correctamente.")

    if current_user.tipo_usuario != "Admin" and flashcard_obj.autor != current_user._id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para eliminar esta flashcard."
        )

    result_delete = dao.eliminar(id_flashcard)  

    if result_delete.get('estatus') == 'ERROR':  
        error_detail = result_delete.get('mensaje', 'Error al eliminar la flashcard')
        status_code_del_error = status.HTTP_404_NOT_FOUND if error_detail == 'Flashcard no existe' else status.HTTP_500_INTERNAL_SERVER_ERROR  
        raise HTTPException(status_code=status_code_del_error, detail=error_detail)  

    return result_delete


@router.get("/", response_model=list[Flashcard])
async def obtener_todas(
        request: Request,
        current_user: UsuarioSelect = Depends(get_current_user)  # Requiere autenticación
):
    if current_user.tipo_usuario != "Admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Solo el administrador puede consultar todas las flashcards.")
    dao = FlashcardsDAO(request.app.db)
    return dao.consultaGeneral()


@router.get("/{id_flashcard}", response_model=Flashcard)
async def obtener_por_id(
        id_flashcard: str,
        request: Request,
        current_user: UsuarioSelect = Depends(get_current_user)  # Requiere autenticación
):
    try:
        ObjectId(id_flashcard)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID de flashcard inválido")

    dao = FlashcardsDAO(request.app.db)
    resultado = dao.consultaPorId(id_flashcard)

    if isinstance(resultado, dict) and (mensaje := resultado.get("mensaje")):
        status_code = status.HTTP_404_NOT_FOUND if "no existe" in mensaje.lower() else status.HTTP_400_BAD_REQUEST
        raise HTTPException(status_code=status_code, detail=mensaje)

    if not isinstance(resultado, Flashcard):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener la flashcard.")

    return resultado

from fastapi import APIRouter, HTTPException, Request
from Model.flashcardModel import FlashcardInsert, FlashcardUpdate, Salida, FlashcardResponse, Flashcard
from dao.flashcardsDAO import FlashcardsDAO
from bson import ObjectId

router = APIRouter(
    prefix="/flashcards",
    tags=["Flashcards"]
)

@router.post("/crear", response_model=Salida)
async def crear_flashcard(flashcard: FlashcardInsert, request: Request):
    dao = FlashcardsDAO(request.app.db)
    return dao.agregar(flashcard)

@router.put("/{id_flashcard}", response_model=FlashcardResponse)
async def actualizar_flashcard(id_flashcard: str, update: FlashcardUpdate, request: Request):
    try:
        ObjectId(id_flashcard)
    except Exception:
        raise HTTPException(status_code=400, detail="ID de flashcard inválido")
    dao = FlashcardsDAO(request.app.db)
    result = dao.actualizar(id_flashcard, update)
    if result.get('mensaje') == 'Flashcard no existe':
        raise HTTPException(status_code=404, detail=result['mensaje'])
    if result.get('mensaje') == 'ID de flashcard inválido':
        raise HTTPException(status_code=400, detail=result['mensaje'])
    return result

@router.delete("/{id_flashcard}", response_model=Salida)
async def eliminar_flashcard(id_flashcard: str, request: Request):
    try:
        ObjectId(id_flashcard)
    except Exception:
        raise HTTPException(status_code=400, detail="ID de flashcard inválido")
    dao = FlashcardsDAO(request.app.db)
    result = dao.eliminar(id_flashcard)
    if result['estatus'] == 'ERROR':
        if result['mensaje'] == 'Flashcard no existe':
            raise HTTPException(status_code=404, detail=result['mensaje'])
        raise HTTPException(status_code=500, detail=result['mensaje'])
    return result

@router.get("/", response_model=list[Flashcard])
async def obtener_todas(request: Request):
    dao = FlashcardsDAO(request.app.db)
    return dao.consultaGeneral()


@router.get("/{id_flashcard}", response_model=Flashcard | dict)
async def obtener_por_id(id_flashcard: str, request: Request):
    try:
        ObjectId(id_flashcard)
    except Exception:
        raise HTTPException(status_code=400, detail="ID de flashcard inválido")

    dao = FlashcardsDAO(request.app.db)
    resultado = dao.consultaPorId(id_flashcard)

    if mensaje := resultado.get("mensaje"):
        raise HTTPException(
            status_code=404 if mensaje == "La flashcard no existe" else 400,
            detail=mensaje
        )
    
    return resultado

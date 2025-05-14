from fastapi import APIRouter, HTTPException, Request
from Model.flashcardModel import FlashcardInsert, Salida
from dao.flashcardsDAO import FlashcardsDAO

router = APIRouter(
    prefix="/flashcards",
    tags=["Flashcards"]
)

@router.post("/crear", response_model=Salida)
async def crear_flashcard(flashcard: FlashcardInsert, request: Request):
    dao = FlashcardsDAO(request.app.db)
    return dao.agregar(flashcard)

@router.delete("/{id_flashcard}", response_model=Salida)
async def eliminar_flashcard(id_flashcard: str, request: Request):
    dao = FlashcardsDAO(request.app.db)
    result = dao.eliminar(id_flashcard)
    if result['estatus'] == 'ERROR' and result['mensaje'] == 'Flashcard no existe':
        raise HTTPException(status_code=404, detail=result['mensaje'])
    return result
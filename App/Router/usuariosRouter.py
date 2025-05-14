from fastapi import APIRouter, Request
from Model.usuariosModel import Usuario, Salida
from dao.usuariosDAO import FlashcardsDAO
from bson import ObjectId

router = APIRouter(
    prefix="/flashcards",
    tags=["Flashcards"]
)

@router.post("/crear", response_model=Salida)
async def crear_flashcard(flashcard: FlashcardInsert, request: Request):
    dao = FlashcardsDAO(request.app.db)
    return dao.agregar(flashcard)
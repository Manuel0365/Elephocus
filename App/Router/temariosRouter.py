from fastapi import APIRouter, Request
from dao.temariosDAO import TemariosDAO
from Model.temariosModel import TemarioInsert, Salida

router = APIRouter(
    prefix="/temarios",
    tags=["Temarios"]
)

#Crear un temario
@router.post("/crearTemario", response_model=Salida)
async def agregarTemario(temario: TemarioInsert, request: Request) -> Salida:
    temarioDao = TemariosDAO(request.app.db)
    return temarioDao.agregarTemario(temario)
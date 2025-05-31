from fastapi import APIRouter, Request
from dao.temariosDAO import TemariosDAO
from Model.temariosModel import TemarioInsert, Salida, TemarioSelect, TemarioSalida, TemarioUpdate

router = APIRouter(
    prefix="/temarios",
    tags=["Temarios"]
)

#Crear un temario
@router.post("/crearTemario", response_model=Salida)
async def agregarTemario(temario: TemarioInsert, request: Request) -> Salida:
    temarioDao = TemariosDAO(request.app.db)
    return temarioDao.agregarTemario(temario)

# Consultar temario por su id
@router.get("/consultarTemario/{idTemario}", response_model=TemarioSelect)
async def consultarTemario(idTemario: str, request: Request) -> TemarioSelect:
    temarioDAO = TemariosDAO(request.app.db)
    return temarioDAO.consultarTemario(idTemario)

# Consultar todos los temarios
@router.get("/", response_model=TemarioSalida)
async def consultaGeneral(request: Request):
    return TemariosDAO(request.app.db).consultaGeneral()

# Eliminar un temario
@router.delete("/eliminarTemario/{idTemario}", response_model=Salida)
async def eliminarTemario(idTemario: str, request: Request) -> Salida:
    temarioDao = TemariosDAO(request.app.db)
    return temarioDao.eliminarTemario(idTemario)

# Actualizar un temario
@router.put("/actualizarTemario/{idTemario}", response_model=Salida)
async def actualizarTemario(idTemario: str, datos: TemarioUpdate, request: Request) -> Salida:
    temarioDao = TemariosDAO(request.app.db)
    return temarioDao.actualizarTemario(idTemario, datos.dict(exclude_unset=True))
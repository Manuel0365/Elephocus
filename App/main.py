import uvicorn
from fastapi import FastAPI
from pymongo import MongoClient
from Router.flashcardsRouter import router as flashcards_router
from Router.usuariosRouter import router as usuarios_router
from Router.temariosRouter import router as temarios_router
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongo_client = MongoClient("mongodb://localhost:27017")
    app.db = app.mongo_client['Elephocus']
    print("Conectado a MongoDB")
    yield
    app.mongo_client.close()
    print("Desconectado de MongoDB")

app = FastAPI(lifespan=lifespan)
app.include_router(flashcards_router)
app.include_router(usuarios_router)
app.include_router(temarios_router)

@app.get("/")
async def root():
    return {"mensaje": "Servicio de Gestión de Flashcards"}

if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', reload=True, lifespan="on")

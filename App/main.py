import uvicorn
from fastapi import FastAPI
from pymongo import MongoClient
from routers.flashcardsRouter import router as flashcards_router

app = FastAPI()
app.include_router(flashcards_router)

@app.on_event("startup")
async def startup():
    app.mongo_client = MongoClient("mongodb://localhost:27017")
    app.db = app.mongo_client['flashcardsdb']
    print("Conectado a MongoDB")

@app.on_event("shutdown")
async def shutdown():
    app.mongo_client.close()
    print("Desconectando MongoDB")

@app.get("/")
async def root():
    return {"mensaje": "Servicio de Gestión de Flashcards"}

if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', reload=True)
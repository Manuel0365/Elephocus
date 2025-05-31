from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/temarios",
    tags=["Temarios"]
)
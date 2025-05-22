from fastapi import APIRouter

from .contato import router as contato_router

main_router = APIRouter()

main_router.include_router(contato_router, prefix="/contatos", tags=["contatos"])
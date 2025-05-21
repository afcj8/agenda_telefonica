from fastapi import APIRouter, Response
from sqlmodel import Session, select

from api.database import SessionDep
from api.models import Contato
from api.serializers import ContatoResponse

router = APIRouter()

@router.get("/contatos", response_model=list[ContatoResponse])
async def listar_contatos(
    *,
    session: Session = SessionDep,
    response: Response
):
    """Lista todos os contatos"""
    contatos = session.exec(select(Contato)).all()
    return contatos
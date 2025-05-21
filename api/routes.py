from fastapi import APIRouter, HTTPException, Response
from sqlmodel import Session, select

from api.database import SessionDep
from api.models import Contato
from api.serializers import ContatoResponse, ContatoRequest

router = APIRouter()

@router.get("/contatos", response_model=list[ContatoResponse])
async def listar_contatos(
    *,
    session: Session = SessionDep,
):
    """Lista todos os contatos"""
    contatos = session.exec(select(Contato)).all()
    return contatos

@router.post("/contatos", response_model=ContatoResponse, status_code=201)
async def criar_contato(
    *,
    contato: ContatoRequest,
    session: Session = SessionDep,
):
    """Cria um novo contato"""
    
    # Verifica se o contato já existe
    contato_existente = session.exec(
        select(Contato).where(Contato.telefone == contato.telefone)
    ).first()
    if contato_existente:
        raise HTTPException(
            status_code=409,
            detail="Contato com este telefone já existe.",
        )
        
    contato_obj = Contato.model_validate(contato)
    session.add(contato_obj)
    session.commit()
    session.refresh(contato_obj)
    return contato_obj

@router.patch("/contatos/{contato_id}", response_model=ContatoResponse, status_code=200)
async def atualizar_contato(
    *,
    contato_id: int,
    contato: ContatoRequest,
    session: Session = SessionDep,
):
    """Atualiza um contato existente"""
    
    contato_obj = session.get(Contato, contato_id)
    
    # Verifica se o contato existe
    if not contato_obj:
        raise HTTPException(
            status_code=404,
            detail="Contato não encontrado.",
        )
    
    # Verifica se o telefone já existe
    contato_existente = session.exec(
        select(Contato).where(Contato.telefone == contato.telefone)
    ).first()
    if contato_existente and contato_existente.id != contato_id:
        raise HTTPException(
            status_code=409,
            detail="Contato com este telefone já existe.",
        )
        
    contato_obj.nome = contato.nome
    contato_obj.telefone = contato.telefone
    contato_obj.email = contato.email   
     
    session.add(contato_obj)
    session.commit()
    session.refresh(contato_obj)
    return contato_obj
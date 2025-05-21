"""Modelo de dados para a API de agenda telefônica."""

from typing import Optional
from sqlmodel import Field, SQLModel

class Contato(SQLModel, table=True):
    """Modelo de dados para um contato na agenda telefônica."""

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(default=None, nullable=False)
    telefone: str = Field(unique=True)
    email: Optional[str] = Field(default=None)
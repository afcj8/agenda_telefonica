""""Modelos de serialização para a API"""

from pydantic import BaseModel
from typing import Optional

class ContatoResponse(BaseModel):
    """Representa o modelo de resposta para um contato."""
    
    id: int
    nome: str
    telefone: str
    email: Optional[str] = None
    
class ContatoRequest(BaseModel):
    """Representa o modelo de requisição para criar um contato."""
    
    nome: str
    telefone: str
    email: Optional[str] = None
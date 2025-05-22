from fastapi import FastAPI
from api.database import create_db_and_tables
from api.routes import router

def lifespan(app: FastAPI):
    """Função de ciclo de vida da aplicação."""
    
    # Executa na inicialização da aplicação
    create_db_and_tables()
    yield  # Separa a inicialização do encerramento
    # Executa no encerramento da aplicação
    pass

app = FastAPI(
    title="Agenda Telefônica API",
    version="0.1.0",
    description="API para gerenciar contatos de uma agenda telefônica",
    lifespan=lifespan,
)

# Inclui as rotas no app
app.include_router(router, tags=["contatos"])
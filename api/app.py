from fastapi import FastAPI
from api.database import create_db_and_tables
from api.routes import router

app = FastAPI(
    title="Agenda Telefônica API",
    version="0.1.0",
    description="API para gerenciar contatos de uma agenda telefônica",
)

@app.on_event("startup")
def on_startup():
    """Executa na inicialização do aplicativo."""
    create_db_and_tables()

@app.on_event("shutdown")
def on_shutdown():
    """Executa no encerramento do aplicativo."""
    pass

# Inclui as rotas no app
app.include_router(router)
from fastapi import FastAPI
from app.routes import dados

app = FastAPI()

# Incluir as rotas
app.include_router(dados.router)

# Mensagem de boas-vindas
@app.get("/")
def read_root():
    return {"mensagem": "API está online! 🚀"}

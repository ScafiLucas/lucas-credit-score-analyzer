import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.api.routes import api_router

load_dotenv()

app = FastAPI(
    title="Lucas Credit Score Analyzer",
    description="API para análise de crédito com processamento assíncrono e IA",
    version="1.0.0"
)

# Libera CORS para testes locais e integração com front
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Roteamento centralizado
app.include_router(api_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}

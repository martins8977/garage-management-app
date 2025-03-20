from app.config import RAPIDAPI_KEY  # Importa para garantir que a variável está carregada
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, customers, vehicles, jobs, tecdoc
from app.database import init_db
import os


app = FastAPI()

# ⚠️ Define aqui os hosts autorizados
origins = [
    "http://localhost:9000",
    "http://192.168.1.252:9000"
]

# ✅ Middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,             # Sem wildcard
    allow_credentials=True,            # Importante para tokens/cookies
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()

API_KEY = os.getenv("RAPIDAPI_KEY")
if not API_KEY:
    raise ValueError("⚠️ RAPIDAPI_KEY não carregada do .env!")

# Routers
app.include_router(auth.router)
app.include_router(customers.router)
app.include_router(vehicles.router)
app.include_router(tecdoc.router)
from dotenv import load_dotenv
import os

# Carrega o .env imediatamente
load_dotenv()

# Lê a variável de ambiente
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

if not RAPIDAPI_KEY:
    raise ValueError("⚠️ RAPIDAPI_KEY não carregada do .env!")
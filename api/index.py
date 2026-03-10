from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
db = {"comando": "SISTEMA CEO-OS ONLINE Y CONECTADO"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Misma ruta para LEER
@app.get("/api")
def leer_comando():
    return db

# Misma ruta exacta para ENVIAR (Vercel no podr? dar 404)
@app.post("/api")
async def recibir_comando(data: dict):
    db["comando"] = data.get("comando", "Comando vac?o")
    return {"status": "ok"}

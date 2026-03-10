from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Memoria volátil del servidor
db = {"comando": "SISTEMA OPENCLAW ONLINE"}

# Evitamos bloqueos de CORS entre tu web y el servidor
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
def leer_comando():
    return db

@app.post("/api/enviar")
async def recibir_comando(data: dict):
    db["comando"] = data.get("comando", "Comando vacío")
    return {"status": "Comando inyectado con éxito"}

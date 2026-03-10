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

# Cubrimos todas las rutas posibles
@app.get("/")
@app.get("/api")
def leer_comando():
    return db

@app.post("/enviar")
@app.post("/api/enviar")
async def recibir_comando(data: dict):
    db["comando"] = data.get("comando", "Comando vacío")
    return {"status": "ok"}

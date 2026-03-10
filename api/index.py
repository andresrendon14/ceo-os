from fastapi import FastAPI
app = FastAPI()

# Guardamos el comando en memoria
db = {"comando": "Sistema Iniciado"}

@app.get("/api")
def root():
    return db

@app.get("/api/comandos")
def get_cmd():
    return db

@app.post("/api/enviar")
async def post_cmd(data: dict):
    db["comando"] = data.get("comando")
    return {"status": "ok"}

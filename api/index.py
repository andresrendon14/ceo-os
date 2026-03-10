from fastapi import FastAPI
app = FastAPI()

@app.get("/api")
def home():
    return {"status": "Sistema Activo", "comando": "Esperando..."}

@app.get("/api/comandos")
def get_cmds():
    return {"comando": "Esperando..."}

@app.post("/api/enviar")
async def post_cmd(data: dict):
    return {"status": "ok"}

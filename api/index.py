from fastapi import FastAPI
app = FastAPI()

# Variable global para guardar el comando en memoria de Vercel
ultimo_comando = {"comando": None}

@app.get("/api")
def read_root():
    return ultimo_comando

@app.get("/api/comandos")
def get_comandos():
    return ultimo_comando

@app.post("/api/enviar")
async def enviar_comando(data: dict):
    global ultimo_comando
    ultimo_comando["comando"] = data.get("comando")
    return {"status": "ok", "recibido": ultimo_comando["comando"]}

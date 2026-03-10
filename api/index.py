from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
queue = []

class Comando(BaseModel):
    instruccion: str

@app.get("/api/comandos")
def obtener_comandos():
    global queue
    if not queue:
        return {"comando": None}
    return {"comando": queue.pop(0)}

@app.post("/api/enviar")
def enviar_comando(cmd: Comando):
    queue.append(cmd.instruccion)
    return {"status": "Enviado al Agente Local", "instruccion": cmd.instruccion}

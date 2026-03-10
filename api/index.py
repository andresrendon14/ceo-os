from fastapi import FastAPI
app = FastAPI()

@app.get("/api/comandos")
def read_root():
    return {"status": "Sistema Los Parceritos Online", "comando": None}

@app.post("/api/enviar")
async def enviar(data: dict):
    return {"status": "Recibido", "data": data}

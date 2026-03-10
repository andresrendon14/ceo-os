from fastapi import FastAPI

app = FastAPI()

@app.get("/api/comandos")
def get_cmd():
    return {"status": "Sistema Online", "comando": None}

@app.post("/api/enviar")
async def post_cmd(data: dict):
    return {"status": "Recibido", "data": data}

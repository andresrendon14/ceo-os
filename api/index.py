from fastapi import FastAPI
app = FastAPI()

# Memoria temporal para el comando
db = {"comando": "Sistema Reiniciado"}

@app.get("/api")
def root():
    return db

@app.post("/api/enviar")
async def post_cmd(data: dict):
    db["comando"] = data.get("comando")
    return {"status": "ok"}

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
import database

# Crear las tablas automáticamente
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Los Parceritos API")

@app.get("/")
def home():
    return {"mensaje": "¡Sistema restablecido y conectado!"}

@app.post("/usuarios/")
def crear_usuario(nombre: str, email: str, tecnologia: str, db: Session = Depends(database.get_db)):
    nuevo_parce = models.Usuario(nombre=nombre, email=email, tecnologia=tecnologia)
    db.add(nuevo_parce)
    db.commit()
    db.refresh(nuevo_parce)
    return {"status": "registrado", "data": nuevo_parce}

@app.get("/usuarios/")
def obtener_usuarios(db: Session = Depends(database.get_db)):
    usuarios = db.query(models.Usuario).all()
    return usuarios

from sqlalchemy import Column, Integer, String
from database import Base  # Eliminamos el punto (.)

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    email = Column(String, unique=True, index=True)
    tecnologia = Column(String)

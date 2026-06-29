from sqlalchemy import Column, Integer, String
from database import Base


class Equipo(Base):
    __tablename__ = "equipos"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True, nullable=False)
    nombre = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    estado = Column(String, default="Disponible")
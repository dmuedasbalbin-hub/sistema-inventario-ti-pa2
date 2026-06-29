from database import Base, engine
from models import Equipo

Base.metadata.create_all(bind=engine)

print("Base de datos creada correctamente.")
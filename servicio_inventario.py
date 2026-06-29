from database import SessionLocal
from models import Equipo

def limpiar_bd():
    session = SessionLocal()
    try:
        session.query(Equipo).delete()
        session.commit()
    finally:
        session.close()


def agregar_equipo_bd(codigo, nombre, categoria):
    session = SessionLocal()

    try:
        if codigo == "" or nombre == "" or categoria == "":
            return False

        equipo_existente = session.query(Equipo).filter_by(codigo=codigo).first()

        if equipo_existente:
            return False

        nuevo_equipo = Equipo(
            codigo=codigo,
            nombre=nombre,
            categoria=categoria,
            estado="Disponible"
        )

        session.add(nuevo_equipo)
        session.commit()
        return True

    finally:
        session.close()

def buscar_equipo_bd(codigo):
    if not codigo:
        return None

    session = SessionLocal()

    try:
        return session.query(Equipo).filter_by(codigo=codigo).first()

    finally:
        session.close()
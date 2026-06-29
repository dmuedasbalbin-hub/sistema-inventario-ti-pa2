from servicio_inventario import (
    agregar_equipo_bd,
    buscar_equipo_bd,
    limpiar_bd,
)


def test_agregar_equipo():
    limpiar_bd()

    resultado = agregar_equipo_bd(
        "PC001",
        "Laptop HP",
        "Laptop"
    )

    assert resultado == True


def test_buscar_equipo_por_codigo():
    limpiar_bd()

    agregar_equipo_bd(
        "PC002",
        "Monitor Samsung",
        "Monitor"
    )

    equipo = buscar_equipo_bd("PC002")

    assert equipo is not None
    assert equipo.codigo == "PC002"
    assert equipo.nombre == "Monitor Samsung"
    assert equipo.categoria == "Monitor"
    assert equipo.estado == "Disponible"
from kata_tdd import validar_codigo_equipo


def test_codigo_valido():
    assert validar_codigo_equipo("PC001") == True
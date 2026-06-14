import json

ARCHIVO_INVENTARIO = "inventario.json"
inventario = []


def cargar_inventario():
    global inventario

    try:
        with open(ARCHIVO_INVENTARIO, "r", encoding="utf-8") as archivo:
            inventario = json.load(archivo)
    except FileNotFoundError:
        inventario = []
    except json.JSONDecodeError:
        print("Error: el archivo de inventario está dañado. Se iniciará vacío.")
        inventario = []


def guardar_inventario():
    try:
        with open(ARCHIVO_INVENTARIO, "w", encoding="utf-8") as archivo:
            json.dump(inventario, archivo, indent=4, ensure_ascii=False)
    except Exception as error:
        print(f"Error al guardar el inventario: {error}")


def existe_codigo(codigo):
    for equipo in inventario:
        if equipo["codigo"] == codigo:
            return True
    return False


def agregar_equipo():
    codigo = input("Ingrese el código del equipo: ").strip()

    if codigo == "":
        print("Error: el código no puede estar vacío.")
        return

    if existe_codigo(codigo):
        print("Error: ese código ya está registrado.")
        return

    nombre = input("Ingrese el nombre del equipo: ").strip()
    categoria = input("Ingrese la categoría del equipo: ").strip()

    if nombre == "" or categoria == "":
        print("Error: el nombre y la categoría no pueden estar vacíos.")
        return

    equipo = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "estado": "Disponible"
    }

    inventario.append(equipo)
    guardar_inventario()
    print("Equipo agregado correctamente.")


def mostrar_equipos():
    print("\n=== INVENTARIO TI ===")

    if len(inventario) == 0:
        print("No hay equipos registrados.")
        return

    for equipo in inventario:
        print(f"Código: {equipo['codigo']}")
        print(f"Nombre: {equipo['nombre']}")
        print(f"Categoría: {equipo['categoria']}")
        print(f"Estado: {equipo['estado']}")
        print("--------------------")


def buscar_equipo():
    codigo_buscado = input("Ingrese el código a buscar: ").strip()
    encontrado = False

    for equipo in inventario:
        if equipo["codigo"] == codigo_buscado:
            print("\n=== EQUIPO ENCONTRADO ===")
            print(f"Código: {equipo['codigo']}")
            print(f"Nombre: {equipo['nombre']}")
            print(f"Categoría: {equipo['categoria']}")
            print(f"Estado: {equipo['estado']}")
            encontrado = True
            break

    if encontrado == False:
        print("No se encontró un equipo con ese código.")


def cambiar_estado():
    codigo_buscado = input("Ingrese el código del equipo: ").strip()
    encontrado = False

    for equipo in inventario:
        if equipo["codigo"] == codigo_buscado:
            print(f"Estado actual: {equipo['estado']}")
            nuevo_estado = input("Ingrese el nuevo estado: ").strip()

            if nuevo_estado == "":
                print("Error: el estado no puede estar vacío.")
                return

            equipo["estado"] = nuevo_estado
            guardar_inventario()
            print("Estado actualizado correctamente.")
            encontrado = True
            break

    if encontrado == False:
        print("No se encontró un equipo con ese código.")


def eliminar_equipo():
    codigo_buscado = input("Ingrese el código del equipo a eliminar: ").strip()
    encontrado = False

    for equipo in inventario:
        if equipo["codigo"] == codigo_buscado:
            inventario.remove(equipo)
            guardar_inventario()
            print("Equipo eliminado correctamente.")
            encontrado = True
            break

    if encontrado == False:
        print("No se encontró un equipo con ese código.")


def menu():
    while True:
        print("\n====================================================")
        print("      SISTEMA DE INVENTARIO DE TECNOLOGÍA - TI")
        print("           Producto Académico N.° 1")
        print("           David Muedas - GRUPO E")
        print("      Trabajo Individual realizado en Python")
        print("====================================================")
        print("1. Agregar equipo")
        print("2. Mostrar equipos")
        print("3. Buscar equipo")
        print("4. Cambiar estado")
        print("5. Eliminar equipo")
        print("6. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: debe ingresar un número.")
            continue

        if opcion == 1:
            agregar_equipo()
        elif opcion == 2:
            mostrar_equipos()
        elif opcion == 3:
            buscar_equipo()
        elif opcion == 4:
            cambiar_estado()
        elif opcion == 5:
            eliminar_equipo()
        elif opcion == 6:
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


cargar_inventario()
menu()
# Mejora futura para validación avanzada de datos
# Función futura para generación de reportes

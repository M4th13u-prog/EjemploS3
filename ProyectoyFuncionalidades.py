# ==============================
# BEAUTY APP - SALÓN DE BELLEZA
# ==============================

citas = []
servicios = ["Corte de cabello", "Manicure", "Pedicure", "Tinte"]


# -------- FUNCIONES --------

def mostrar_servicios():
    print("\n--- SERVICIOS DISPONIBLES ---")
    for i, servicio in enumerate(servicios, start=1):
        print(f"{i}. {servicio}")


def registrar_cita():
    print("\n--- REGISTRAR CITA ---")

    nombre = input("Nombre del cliente: ").strip()
    if not nombre:
        print("❌ El nombre no puede estar vacío\n")
        return

    mostrar_servicios()

    try:
        opcion = int(input("Seleccione servicio: "))
        if opcion < 1 or opcion > len(servicios):
            print("❌ Servicio inválido\n")
            return
    except ValueError:
        print("❌ Debe ingresar un número válido\n")
        return

    hora = input("Ingrese hora (ej: 3pm): ").strip()
    if not hora:
        print("❌ La hora no puede estar vacía\n")
        return

    cita = {
        "cliente": nombre,
        "servicio": servicios[opcion - 1],
        "hora": hora,
        "estado": "Pendiente"
    }

    citas.append(cita)
    print("✅ Cita registrada correctamente\n")


def ver_citas():
    print("\n--- LISTA DE CITAS ---")

    if not citas:
        print("❌ No hay citas registradas\n")
        return

    for i, cita in enumerate(citas, start=1):
        print(f"""
Cita {i}
Cliente: {cita['cliente']}
Servicio: {cita['servicio']}
Hora: {cita['hora']}
Estado: {cita['estado']}
--------------------------""")


def atender_cita():
    print("\n--- ATENDER CITA ---")

    if not citas:
        print("❌ No hay citas disponibles\n")
        return

    for i, cita in enumerate(citas, start=1):
        print(f"{i}. {cita['cliente']} - {cita['estado']}")

    try:
        opcion = int(input("Seleccione cita: "))
        if opcion < 1 or opcion > len(citas):
            print("❌ Opción inválida\n")
            return
    except ValueError:
        print("❌ Debe ingresar un número válido\n")
        return

    if citas[opcion - 1]["estado"] == "Atendido":
        print("⚠️ Esta cita ya fue atendida\n")
        return

    citas[opcion - 1]["estado"] = "Atendido"
    print("💇 Cita atendida correctamente\n")


def eliminar_cita():
    print("\n--- ELIMINAR CITA ---")

    if not citas:
        print("❌ No hay citas\n")
        return

    for i, cita in enumerate(citas, start=1):
        print(f"{i}. {cita['cliente']} - {cita['servicio']}")

    try:
        opcion = int(input("Seleccione cita a eliminar: "))
        if opcion < 1 or opcion > len(citas):
            print("❌ Opción inválida\n")
            return
    except ValueError:
        print("❌ Debe ingresar un número válido\n")
        return

    citas.pop(opcion - 1)
    print("🗑️ Cita eliminada correctamente\n")


# -------- MENÚ PRINCIPAL --------

def menu():
    while True:
        print("""
======= BEAUTY APP =======
1. Registrar cita
2. Ver citas
3. Atender cita
4. Eliminar cita
5. Salir
==========================
""")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_cita()
        elif opcion == "2":
            ver_citas()
        elif opcion == "3":
            atender_cita()
        elif opcion == "4":
            eliminar_cita()
        elif opcion == "5":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida\n")


# -------- EJECUCIÓN --------

if __name__ == "__main__":
    menu()
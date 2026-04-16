# Sistema de Delivery - FastDelivery App

pedidos = []
repartidores = ["Juan", "Carlos", "Luis"]

def registrar_pedido():
    print("\n--- REGISTRAR PEDIDO ---")
    nombre = input("Nombre del cliente: ").strip()
    producto = input("Producto a pedir: ").strip()
    direccion = input("Dirección: ").strip()

    if not nombre or not producto or not direccion:
        print("❌ Todos los campos son obligatorios\n")
        return

    pedido = {
        "cliente": nombre,
        "producto": producto,
        "direccion": direccion,
        "estado": "Pendiente",
        "repartidor": None
    }

    pedidos.append(pedido)
    print("✅ Pedido registrado correctamente\n")


def asignar_repartidor():
    print("\n--- ASIGNAR REPARTIDOR ---")

    if not pedidos:
        print("❌ No hay pedidos\n")
        return

    for i, p in enumerate(pedidos):
        print(f"{i+1}. {p['cliente']} - {p['producto']} (Estado: {p['estado']})")

    try:
        opcion = int(input("Seleccione pedido: ")) - 1
        if opcion < 0 or opcion >= len(pedidos):
            print("❌ Opción inválida\n")
            return
    except:
        print("❌ Debe ingresar un número\n")
        return

    if pedidos[opcion]["estado"] != "Pendiente":
        print("⚠️ Este pedido ya fue asignado o entregado\n")
        return

    for i, r in enumerate(repartidores):
        print(f"{i+1}. {r}")

    try:
        rep = int(input("Seleccione repartidor: ")) - 1
        if rep < 0 or rep >= len(repartidores):
            print("❌ Repartidor inválido\n")
            return
    except:
        print("❌ Debe ingresar un número\n")
        return

    pedidos[opcion]["repartidor"] = repartidores[rep]
    pedidos[opcion]["estado"] = "En camino"

    print("🚚 Repartidor asignado correctamente\n")


def entregar_pedido():
    print("\n--- ENTREGAR PEDIDO ---")

    if not pedidos:
        print("❌ No hay pedidos\n")
        return

    for i, p in enumerate(pedidos):
        print(f"{i+1}. {p['cliente']} - {p['estado']}")

    try:
        opcion = int(input("Seleccione pedido a entregar: ")) - 1
        if opcion < 0 or opcion >= len(pedidos):
            print("❌ Opción inválida\n")
            return
    except:
        print("❌ Debe ingresar un número\n")
        return

    if pedidos[opcion]["estado"] != "En camino":
        print("⚠️ Solo se pueden entregar pedidos en camino\n")
        return

    pedidos[opcion]["estado"] = "Entregado"
    print("📦 Pedido entregado\n")


def ver_pedidos():
    print("\n--- LISTA DE PEDIDOS ---")

    if not pedidos:
        print("❌ No hay pedidos\n")
        return

    for i, p in enumerate(pedidos):
        print(f"""
Pedido {i+1}
Cliente: {p['cliente']}
Producto: {p['producto']}
Dirección: {p['direccion']}
Estado: {p['estado']}
Repartidor: {p['repartidor']}
---------------------------""")


def menu():
    while True:
        print("""
=== FAST DELIVERY APP ===
1. Registrar pedido
2. Asignar repartidor
3. Entregar pedido
4. Ver pedidos
5. Salir
""")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_pedido()
        elif opcion == "2":
            asignar_repartidor()
        elif opcion == "3":
            entregar_pedido()
        elif opcion == "4":
            ver_pedidos()
        elif opcion == "5":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida\n")


# Ejecutar programa
menu()
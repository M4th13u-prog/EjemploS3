# PROYECTO: SISTEMA DE CONTROL DE PAGOS - SALON DE BELLEZA

# Listas para almacenar datos
clientes = []
servicios = []
pagos = []

def menu():
    print("\n=== SALON DE BELLEZA - CONTROL DE PAGOS ===")
    print("1. Registrar cliente")
    print("2. Registrar servicio")
    print("3. Registrar pago")
    print("4. Ver historial de pagos")
    print("5. Ver resumen general")
    print("6. Salir")

def registrar_cliente():
    nombre = input("Nombre del cliente: ")
    clientes.append(nombre)
    print("Cliente registrado correctamente.")

def registrar_servicio():
    servicio = input("Nombre del servicio (corte, tinte, manicure, etc): ")
    precio = float(input("Precio del servicio: "))
    servicios.append({"servicio": servicio, "precio": precio})
    print("Servicio registrado correctamente.")

def registrar_pago():
    if not clientes or not servicios:
        print("Primero registra clientes y servicios.")
        return

    print("\nClientes:")
    for i, c in enumerate(clientes):
        print(f"{i+1}. {c}")

    cliente_index = int(input("Seleccione cliente: ")) - 1

    print("\nServicios:")
    for i, s in enumerate(servicios):
        print(f"{i+1}. {s['servicio']} - S/ {s['precio']}")

    servicio_index = int(input("Seleccione servicio: ")) - 1

    cliente = clientes[cliente_index]
    servicio = servicios[servicio_index]["servicio"]
    precio = servicios[servicio_index]["precio"]

    pagos.append({
        "cliente": cliente,
        "servicio": servicio,
        "precio": precio
    })

    print("Pago registrado correctamente.")

def ver_pagos():
    print("\n=== HISTORIAL DE PAGOS ===")
    for p in pagos:
        print(f"Cliente: {p['cliente']} | Servicio: {p['servicio']} | Pago: S/ {p['precio']}")

def resumen():
    total = sum(p["precio"] for p in pagos)

    print("\n=== RESUMEN GENERAL ===")
    print(f"Total de clientes: {len(clientes)}")
    print(f"Total de servicios registrados: {len(servicios)}")
    print(f"Total de ingresos: S/ {total}")

# Programa principal
while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_cliente()
    elif opcion == "2":
        registrar_servicio()
    elif opcion == "3":
        registrar_pago()
    elif opcion == "4":
        ver_pagos()
    elif opcion == "5":
        resumen()
    elif opcion == "6":
        print("Sistema finalizado.")
        break
    else:
        print("Opción inválida.")
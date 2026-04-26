# PROYECTO: SISTEMA DE CONTROL DE PAGOS - SALON DE BELLEZA (VERSION PRO)

from datetime import datetime

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
    print("✅ Cliente registrado.")

def registrar_servicio():
    nombre = input("Nombre del servicio: ")
    precio = float(input("Precio (S/): "))
    servicios.append({"nombre": nombre, "precio": precio})
    print("✅ Servicio registrado.")

def registrar_pago():
    if not clientes or not servicios:
        print("⚠️ Debes registrar clientes y servicios primero.")
        return

    print("\nClientes:")
    for i, c in enumerate(clientes):
        print(f"{i+1}. {c}")
    c_index = int(input("Seleccione cliente: ")) - 1

    print("\nServicios:")
    for i, s in enumerate(servicios):
        print(f"{i+1}. {s['nombre']} - S/ {s['precio']}")
    s_index = int(input("Seleccione servicio: ")) - 1

    cliente = clientes[c_index]
    servicio = servicios[s_index]["nombre"]
    precio = servicios[s_index]["precio"]

    print("\nMétodos de pago:")
    print("1. Efectivo")
    print("2. Yape")
    print("3. Tarjeta")
    print("4. Transferencia")

    metodo_op = input("Seleccione método de pago: ")

    if metodo_op == "1":
        metodo = "Efectivo"
    elif metodo_op == "2":
        metodo = "Yape"
    elif metodo_op == "3":
        metodo = "Tarjeta"
    elif metodo_op == "4":
        metodo = "Transferencia"
    else:
        metodo = "Desconocido"

    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

    pagos.append({
        "cliente": cliente,
        "servicio": servicio,
        "precio": precio,
        "metodo": metodo,
        "fecha": fecha
    })

    print("✅ Pago registrado correctamente.")

def ver_pagos():
    print("\n=== HISTORIAL DE PAGOS ===")
    for p in pagos:
        print(f"{p['fecha']} | {p['cliente']} | {p['servicio']} | S/ {p['precio']} | {p['metodo']}")

def resumen():
    total = sum(p["precio"] for p in pagos)

    metodos = {}
    for p in pagos:
        if p["metodo"] in metodos:
            metodos[p["metodo"]] += p["precio"]
        else:
            metodos[p["metodo"]] = p["precio"]

    print("\n=== RESUMEN GENERAL ===")
    print(f"Total de clientes: {len(clientes)}")
    print(f"Total de servicios: {len(servicios)}")
    print(f"Total de ingresos: S/ {total}")

    print("\nIngresos por método de pago:")
    for m, monto in metodos.items():
        print(f"{m}: S/ {monto}")

# PROGRAMA PRINCIPAL
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
        print("👋 Sistema cerrado.")
        break
    else:
        print("❌ Opción inválida.")
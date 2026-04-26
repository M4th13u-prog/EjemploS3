# SISTEMA PROFESIONAL - SALON DE BELLEZA
# CONTROL DE PAGOS Y SERVICIOS

from datetime import datetime

# Datos iniciales (SERVICIOS CON PRECIOS)
servicios = [
    {"nombre": "Corte de cabello", "precio": 15},
    {"nombre": "Tinte", "precio": 40},
    {"nombre": "Manicure", "precio": 20},
    {"nombre": "Pedicure", "precio": 25},
    {"nombre": "Peinado", "precio": 30}
]

clientes = []
pagos = []

# FUNCIONES
def limpiar():
    print("\n" * 3)

def pausa():
    input("\nPresiona ENTER para continuar...")

def menu():
    limpiar()
    print("======================================")
    print("   💇‍♀️ SALON DE BELLEZA - SISTEMA")
    print("======================================")
    print("1. Registrar cliente")
    print("2. Ver servicios")
    print("3. Registrar pago")
    print("4. Ver historial")
    print("5. Ver resumen")
    print("6. Salir")
    print("======================================")

def registrar_cliente():
    limpiar()
    print("=== REGISTRO DE CLIENTE ===")
    nombre = input("Ingrese nombre: ").strip()

    if nombre == "":
        print("❌ Nombre inválido")
    else:
        clientes.append(nombre)
        print("✅ Cliente registrado")

    pausa()

def ver_servicios():
    limpiar()
    print("=== LISTA DE SERVICIOS ===")
    for i, s in enumerate(servicios, 1):
        print(f"{i}. {s['nombre']} - S/ {s['precio']}")
    pausa()

def elegir_cliente():
    if not clientes:
        print("❌ No hay clientes registrados")
        pausa()
        return None

    print("\nClientes:")
    for i, c in enumerate(clientes, 1):
        print(f"{i}. {c}")

    try:
        op = int(input("Seleccione cliente: "))
        return clientes[op - 1]
    except:
        print("❌ Selección inválida")
        pausa()
        return None

def elegir_servicio():
    print("\nServicios:")
    for i, s in enumerate(servicios, 1):
        print(f"{i}. {s['nombre']} - S/ {s['precio']}")

    try:
        op = int(input("Seleccione servicio: "))
        return servicios[op - 1]
    except:
        print("❌ Selección inválida")
        pausa()
        return None

def elegir_metodo():
    print("\nMétodo de pago:")
    print("1. Efectivo")
    print("2. Yape")
    print("3. Tarjeta")
    print("4. Transferencia")

    opciones = {
        "1": "Efectivo",
        "2": "Yape",
        "3": "Tarjeta",
        "4": "Transferencia"
    }

    op = input("Seleccione: ")
    return opciones.get(op, "Desconocido")

def registrar_pago():
    limpiar()
    print("=== REGISTRO DE PAGO ===")

    cliente = elegir_cliente()
    if not cliente:
        return

    servicio = elegir_servicio()
    if not servicio:
        return

    metodo = elegir_metodo()
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

    pagos.append({
        "cliente": cliente,
        "servicio": servicio["nombre"],
        "precio": servicio["precio"],
        "metodo": metodo,
        "fecha": fecha
    })

    print("\n✅ Pago registrado correctamente")
    pausa()

def ver_historial():
    limpiar()
    print("=== HISTORIAL DE PAGOS ===")

    if not pagos:
        print("No hay pagos registrados")
    else:
        for p in pagos:
            print(f"{p['fecha']} | {p['cliente']} | {p['servicio']} | S/ {p['precio']} | {p['metodo']}")

    pausa()

def resumen():
    limpiar()
    print("=== RESUMEN GENERAL ===")

    total = sum(p["precio"] for p in pagos)

    print(f"Clientes registrados: {len(clientes)}")
    print(f"Total ingresos: S/ {total}")

    metodos = {}
    for p in pagos:
        metodos[p["metodo"]] = metodos.get(p["metodo"], 0) + p["precio"]

    print("\nIngresos por método:")
    for m, v in metodos.items():
        print(f"{m}: S/ {v}")

    pausa()

# PROGRAMA PRINCIPAL
while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_cliente()
    elif opcion == "2":
        ver_servicios()
    elif opcion == "3":
        registrar_pago()
    elif opcion == "4":
        ver_historial()
    elif opcion == "5":
        resumen()
    elif opcion == "6":
        print("\n👋 Gracias por usar el sistema")
        break
    else:
        print("❌ Opción inválida")
        pausa()
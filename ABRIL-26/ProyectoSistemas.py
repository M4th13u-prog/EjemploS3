import json
from datetime import datetime

# ARCHIVOS
ARCHIVO_PRODUCTOS = "productos.json"
ARCHIVO_VENTAS = "ventas.json"

# CARGAR DATOS
def cargar_datos():
    try:
        with open(ARCHIVO_PRODUCTOS, "r") as f:
            productos = json.load(f)
    except:
        productos = []

    try:
        with open(ARCHIVO_VENTAS, "r") as f:
            ventas = json.load(f)
    except:
        ventas = []

    return productos, ventas

def guardar_datos(productos, ventas):
    with open(ARCHIVO_PRODUCTOS, "w") as f:
        json.dump(productos, f, indent=4)

    with open(ARCHIVO_VENTAS, "w") as f:
        json.dump(ventas, f, indent=4)

# =========================
# MENU
# =========================
def menu():
    print("\n========== BOTICA PRO ==========")
    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Realizar venta")
    print("4. Ver historial")
    print("5. Reporte diario")
    print("6. Salir")

# =========================
# PRODUCTOS
# =========================
def registrar_producto(productos):
    print("\n--- NUEVO PRODUCTO ---")
    codigo = input("Código: ")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))
    vencimiento = input("Fecha vencimiento: ")

    productos.append({
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "vencimiento": vencimiento
    })

    print("✅ Producto registrado")

def buscar_producto(productos):
    palabra = input("Buscar producto: ").lower()

    encontrados = [p for p in productos if palabra in p["nombre"].lower()]

    if not encontrados:
        print("❌ No encontrado")
        return None

    for p in encontrados:
        print(f"{p['codigo']} | {p['nombre']} | S/ {p['precio']} | Stock: {p['stock']}")

    return encontrados[0]

# =========================
# BOLETA
# =========================
def generar_boleta(venta):
    print("\n====== BOLETA ======")
    print(f"N° Venta: {venta['nro']}")
    print(f"Fecha: {venta['fecha']}")
    print(f"Producto: {venta['producto']}")
    print(f"Cantidad: {venta['cantidad']}")
    print(f"Total: S/ {venta['total']}")
    print("====================")

# =========================
# VENTA
# =========================
def realizar_venta(productos, ventas):
    producto = buscar_producto(productos)

    if not producto:
        return

    cantidad = int(input("Cantidad: "))

    if cantidad > producto["stock"]:
        print("❌ Stock insuficiente")
        return

    total = cantidad * producto["precio"]
    producto["stock"] -= cantidad

    venta = {
        "nro": len(ventas) + 1,
        "producto": producto["nombre"],
        "cantidad": cantidad,
        "total": total,
        "fecha": datetime.now().strftime("%d/%m/%Y")
    }

    ventas.append(venta)

    generar_boleta(venta)

# =========================
# HISTORIAL
# =========================
def historial(ventas):
    print("\n--- HISTORIAL ---")
    for v in ventas:
        print(v)

# =========================
# REPORTE DIARIO
# =========================
def reporte_diario(ventas):
    hoy = datetime.now().strftime("%d/%m/%Y")
    total = 0

    print("\n--- REPORTE DEL DÍA ---")

    for v in ventas:
        if v["fecha"] == hoy:
            print(v)
            total += v["total"]

    print(f"\nTOTAL DEL DÍA: S/ {total}")

# =========================
# MAIN
# =========================
productos, ventas = cargar_datos()

while True:
    menu()
    op = input("Opción: ")

    if op == "1":
        registrar_producto(productos)
    elif op == "2":
        buscar_producto(productos)
    elif op == "3":
        realizar_venta(productos, ventas)
    elif op == "4":
        historial(ventas)
    elif op == "5":
        reporte_diario(ventas)
    elif op == "6":
        guardar_datos(productos, ventas)
        print("💾 Datos guardados. Hasta luego")
        break
    else:
        print("❌ Opción inválida")
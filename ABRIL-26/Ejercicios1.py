# SISTEMA DE VENTAS PARA BOTICA

from datetime import datetime

clientes = []
productos = []
ventas = []

# =========================
# MENU
# =========================
def menu():
    print("\n========== BOTICA - SISTEMA DE VENTAS ==========")
    print("1. Registrar cliente")
    print("2. Registrar producto")
    print("3. Realizar venta")
    print("4. Ver historial de ventas")
    print("5. Ver stock de productos")
    print("6. Salir")

# =========================
# CLIENTES
# =========================
def registrar_cliente():
    print("\n--- REGISTRO DE CLIENTE ---")
    dni = input("DNI: ")
    nombre = input("Nombre: ")
    celular = input("Celular: ")

    clientes.append({
        "dni": dni,
        "nombre": nombre,
        "celular": celular
    })

    print("✅ Cliente registrado")

# =========================
# PRODUCTOS
# =========================
def registrar_producto():
    print("\n--- REGISTRO DE PRODUCTO ---")
    codigo = input("Código: ")
    nombre = input("Producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Stock: "))
    vencimiento = input("Fecha de vencimiento: ")
    tipo = input("Tipo (pastilla/jarabe): ")
    laboratorio = input("Laboratorio: ")

    productos.append({
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": cantidad,
        "vencimiento": vencimiento,
        "tipo": tipo,
        "laboratorio": laboratorio
    })

    print("✅ Producto registrado")

# =========================
# BUSCAR PRODUCTO
# =========================
def buscar_producto():
    codigo = input("Ingrese código del producto: ")

    for p in productos:
        if p["codigo"] == codigo:
            return p

    return None

# =========================
# VENTA
# =========================
def realizar_venta():
    print("\n--- REGISTRO DE VENTA ---")

    if not productos:
        print("❌ No hay productos registrados")
        return

    producto = buscar_producto()

    if not producto:
        print("❌ Producto no encontrado")
        return

    print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Stock: {producto['stock']}")

    cantidad = int(input("Cantidad a comprar: "))

    if cantidad > producto["stock"]:
        print("❌ No hay suficiente stock")
        return

    subtotal = cantidad * producto["precio"]
    total = subtotal  # (puedes agregar IGV si quieres)

    producto["stock"] -= cantidad

    nro_venta = len(ventas) + 1
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

    ventas.append({
        "nro": nro_venta,
        "producto": producto["nombre"],
        "cantidad": cantidad,
        "precio": producto["precio"],
        "subtotal": subtotal,
        "total": total,
        "fecha": fecha
    })

    print("✅ Venta realizada correctamente")
    print(f"Total a pagar: S/ {total}")

# =========================
# HISTORIAL
# =========================
def historial_ventas():
    print("\n--- HISTORIAL DE VENTAS ---")

    if not ventas:
        print("No hay ventas registradas")
        return

    for v in ventas:
        print(f"N°{v['nro']} | {v['fecha']} | {v['producto']} | Cant: {v['cantidad']} | Total: S/ {v['total']}")

# =========================
# STOCK
# =========================
def ver_stock():
    print("\n--- STOCK DE PRODUCTOS ---")

    if not productos:
        print("No hay productos registrados")
        return

    for p in productos:
        print(f"{p['codigo']} | {p['nombre']} | Stock: {p['stock']} | Vence: {p['vencimiento']}")

# =========================
# MAIN
# =========================
while True:
    menu()
    opcion = input("Seleccione opción: ")

    if opcion == "1":
        registrar_cliente()
    elif opcion == "2":
        registrar_producto()
    elif opcion == "3":
        realizar_venta()
    elif opcion == "4":
        historial_ventas()
    elif opcion == "5":
        ver_stock()
    elif opcion == "6":
        print("👋 Sistema finalizado")
        break
    else:
        print("❌ Opción inválida")
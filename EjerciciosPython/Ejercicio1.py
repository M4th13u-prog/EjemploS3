# EJERCICIO: Sistema de Gestión de Inventario Escolar
# Objetivo: Crear un programa que permita agregar, ver y calcular el valor de productos.

def mostrar_menu():
    print("\n--- SISTEMA DE INVENTARIO ---")
    print("1. Agregar producto")
    print("2. Ver inventario")
    print("3. Calcular valor total")
    print("4. Salir")

def ejecutar_sistema():
    inventario = []
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio por unidad: "))
            cantidad = int(input("Cantidad en stock: "))
            
            producto = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            }
            inventario.append(producto)
            print(f"¡{nombre} agregado con éxito!")

        elif opcion == "2":
            print("\n--- Lista de Productos ---")
            if not inventario:
                print("El inventario está vacío.")
            for p in inventario:
                print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Stock: {p['cantidad']}")

        elif opcion == "3":
            total = sum(p['precio'] * p['cantidad'] for p in inventario)
            print(f"\nEl valor total del inventario es: ${total:.2f}")

        elif opcion == "4":
            print("Saliendo del sistema... ¡Adiós!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    ejecutar_sistema()
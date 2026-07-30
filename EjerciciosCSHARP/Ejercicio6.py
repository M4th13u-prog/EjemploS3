# Inicializar la lista para los precios y la variable de posición
precios = []
posicion = -1

# Ingreso de los 5 precios iniciales (Equivalente al primer PARA)
print("--- Registro de Precios ---")
for i in range(5):
    precio_ingresado = float(input(f"Ingrese el precio para la posición {i}: "))
    precios.append(precio_ingresado)

# Ingreso del precio a buscar
buscado = float(input("\nIngrese el precio exacto a buscar: "))

# Búsqueda del precio en la lista (Equivalente al segundo PARA)
for i in range(5):
    if precios[i] == buscado:
        posicion = i
        # Nota: En Python podrías agregar un 'break' aquí para detener 
        # la búsqueda una vez que lo encuentras y ahorrar recursos.

# Verificación y actualización (Equivalente al bloque SI...SINO)
if posicion != -1:
    nuevo = float(input(f"\nPrecio encontrado. Ingrese el NUEVO precio para reemplazarlo: "))
    precios[posicion] = nuevo
    print("Precio actualizado")
else:
    print("\nPrecio no encontrado")

# Mostrar el resultado final (Equivalente al último PARA)
print("\n--- Lista de Precios Final ---")
for i in range(5):
    print(f"Posición {i}: {precios[i]}")
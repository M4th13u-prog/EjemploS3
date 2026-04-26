n = int(input("Ingrese número de días: "))

total = 0
mayor = -1
menor = float("inf")
dia_mayor = 0
dia_menor = 0

excelente = bueno = regular = malo = 0

for i in range(1, n + 1):
    venta = float(input(f"Día {i} - Venta: S/ "))
    
    total += venta

    if venta > mayor:
        mayor = venta
        dia_mayor = i

    if venta < menor:
        menor = venta
        dia_menor = i

    # Clasificación
    if venta >= 500:
        excelente += 1
    elif venta >= 200:
        bueno += 1
    elif venta >= 50:
        regular += 1
    else:
        malo += 1

promedio = total / n

print("\n=== RESULTADOS ===")
print(f"Total vendido: S/ {total:.2f}")
print(f"Promedio diario: S/ {promedio:.2f}")
print(f"Mayor venta: Día {dia_mayor} con S/ {mayor}")
print(f"Menor venta: Día {dia_menor} con S/ {menor}")

print("\nClasificación:")
print(f"Excelente: {excelente}")
print(f"Bueno: {bueno}")
print(f"Regular: {regular}")
print(f"Malo: {malo}")
kwh = float(input("Ingrese consumo en kWh: "))
total = 0

if kwh <= 100:
    total = kwh * 0.50
elif kwh <= 300:
    total = (100 * 0.50) + ((kwh - 100) * 0.75)
else:
    total = (100 * 0.50) + (200 * 0.75) + ((kwh - 300) * 1.20)

print(f"Total a pagar: S/ {total:.2f}")
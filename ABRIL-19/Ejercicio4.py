categoria = input("Ingrese categoría (A/B): ")
años = int(input("Ingrese años de servicio: "))
sueldo = 1000

if categoria == "A":
    if años >= 5:
        bono = 200
    else:
        bono = 100
else:
    if años >= 5:
        bono = 150
    else:
        bono = 50

total = sueldo + bono

print("Sueldo final:", total)
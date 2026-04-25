prom = float(input("Ingrese promedio: "))

if prom < 0 or prom > 20:
    print("Valor inválido")
elif prom < 10:
    print("Malo")
elif prom < 14:
    print("Regular")
elif prom < 15:
    print("Bueno")
else:
    print("Excelente")
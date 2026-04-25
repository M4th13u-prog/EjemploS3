parcial = float(input("Parcial: "))
final = float(input("Final: "))
p1 = float(input("P1: "))
p2 = float(input("P2: "))
p3 = float(input("P3: "))

prom_prac = (p1 + p2 + p3 - min(p1, p2, p3)) / 2
prom_final = (parcial + final + prom_prac) / 3

print("Promedio final:", prom_final)

if prom_final >= 18:
    print("Excelente")
elif prom_final >= 14:
    print("Bueno")
elif prom_final >= 10:
    print("Regular")
else:
    print("Deficiente")
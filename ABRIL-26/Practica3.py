precio = 5.00

print("Cantidad | Total | Descuento aplicado")

for i in range(1, 21):
    total = i * precio
    
    if 6 <= i <= 12:
        total *= 0.90  # 10% descuento
        desc = "10%"
    elif i > 12:
        total *= 0.80  # 20% descuento
        desc = "20%"
    else:
        desc = "0%"
    
    print(f"{i}        | S/ {total:.2f} | {desc}")
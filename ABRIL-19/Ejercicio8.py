monto = float(input("Ingrese el monto de la compra: "))

if monto >= 100:
    descuento = monto * 0.10
else:
    descuento = 0

total = monto - descuento

print("Total a pagar:", total)
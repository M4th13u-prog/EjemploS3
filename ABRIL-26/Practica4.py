n = int(input("Ingrese cantidad de empleados: "))
total_planilla = 0

for i in range(n):
    print(f"\nEmpleado {i+1}")
    nombre = input("Nombre: ")
    horas = float(input("Horas trabajadas: "))

    if horas <= 160:
        sueldo_bruto = horas * 12.50
        horas_extra = 0
    else:
        horas_extra = horas - 160
        sueldo_bruto = (160 * 12.50) + (horas_extra * 25)

    descuento = sueldo_bruto * 0.05
    sueldo_neto = sueldo_bruto - descuento

    total_planilla += sueldo_neto

    print("-----")
    print(f"Nombre: {nombre}")
    print(f"Horas normales: {horas - horas_extra}")
    print(f"Horas extra: {horas_extra}")
    print(f"Sueldo bruto: S/ {sueldo_bruto:.2f}")
    print(f"Descuento: S/ {descuento:.2f}")
    print(f"Sueldo neto: S/ {sueldo_neto:.2f}")

print(f"\n💰 Total planilla: S/ {total_planilla:.2f}")
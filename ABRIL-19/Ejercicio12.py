edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Acceso permitido")
else:
    faltan = abs(18 - edad)
    print("Acceso denegado. Te faltan", faltan, "años")
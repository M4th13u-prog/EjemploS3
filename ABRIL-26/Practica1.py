edad = int(input("Ingrese edad: "))

if edad < 0:
    print("❌ Edad inválida")
elif 0 <= edad <= 5:
    print("✅ Viaja gratis, no necesita medio pasaje")
elif 6 <= edad <= 17:
    carnet = input("¿Tiene carnet de estudiante? (si/no): ").lower()
    
    if carnet == "si":
        print("✅ Accede al medio pasaje")
    else:
        print("❌ No accede al beneficio")
else:
    print("❌ No accede al medio pasaje")
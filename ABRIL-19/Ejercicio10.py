peso = float(input("Ingrese su peso (kg): "))
estatura = float(input("Ingrese su estatura (m): "))

imc = peso / (estatura ** 2)

print("IMC:", round(imc, 2))

if imc < 18.5:
    print("Bajo peso")
elif imc < 25:
    print("Normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")
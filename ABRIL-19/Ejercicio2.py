opcion = int(input("Ingrese una opción (1-3): "))

match opcion:
    case 1:
        print("Elegiste opción 1")
    case 2:
        print("Elegiste opción 2")
    case 3:
        print("Elegiste opción 3")
    case _:
        print("Opción inválida")
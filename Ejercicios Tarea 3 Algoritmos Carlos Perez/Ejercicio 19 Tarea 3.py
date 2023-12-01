# Ejercicio Carlos Perez
# Ejercicio 19

def dimeTipoMotor():
    opcion = int(input("Ingrese el tipo de motor (1, 2, 3, 4): "))

    if opcion == 0:
        print("No hay establecido un valor definido para el tipo de bomba.")

    elif opcion == 1:
        print("La bomba es una bomba de agua.")

    elif opcion == 2:
        print("La bomba es una bomba de gasolina.")

    elif opcion == 3:
        print("La bomba es una bomba de hormigón.")

    elif opcion == 4:
        print("La bomba es una bomba de pasta alimenticia.")

    else:
        print("No existe un valor válido para tipo de bomba.")


dimeTipoMotor()
# Ejercicio Carlos Perez 
# Ejercicio 12

x = int (input ("Ingrese su edad: "))
nota = float (input ("Ingrese su nota: "))
genero = input ("Ingrese su genero F (Femenino), M (Masculino): ")

char1 = "F"

if x >= 18 and nota >= 5:
    if genero == char1: 
        print ("Aceptada")
    else:
        print ("Posible")
else: 
    print ("No aceptada")
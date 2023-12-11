# Calculadora
# Carlos Perez

print ("---Bienvenido---")
print ("Selecciona la operacion que quieres hacer: ")
print ("1. Suma")
print ("2. Resta")
print ("3. Multiplicacion")
print ("4. Division")
print ("5. Potencia")
print ("6. Modulo")

opcion = int (input ("Ingrese el numero de su seleccion: "))

if opcion == 1:
    num1 = float (input ("Ingrese el numero: "))
    num2 = float (input ("Ingrese el numero: "))
    suma = num1 + num2
    print ("La suma es: ",suma)
elif opcion == 2:
    num1 = float (input ("Ingrese el numero: "))
    num2 = float (input ("Ingrese el numero: "))
    resta = num1 - num2
    print ("La suma es: ",resta)
elif opcion == 3:
    num1 = float (input ("Ingrese el numero: "))
    num2 = float (input ("Ingrese el numero: "))
    multiplicacion = num1 + num2
    print ("La suma es: ",multiplicacion)
elif opcion == 4: 
    num1 = float (input ("Ingrese el numero: "))
    num2 = float (input ("Ingrese el numero: "))
    if num2 == 0:
        print ("No se puede dividir para cero")
    else: 
        division = num1 / num2
        print ("La division es: ",division)
elif opcion == 5: 
    num = float (input ("Ingrese el numero: "))
    potencia = int (input ("Ingrese el numero al que desea elevar"))
    respuesta = num ** potencia
    print ("La potencia es: ",respuesta)
elif opcion == 6:
    num1 = float (input ("Ingrese el numero: "))
    num2 = float (input ("Ingrese el numero: "))
    if num2 == 0:
        print ("No se puede dividir para cero")
    else: 
        modulo = num1 % num2
        print ("La division es: ",modulo)
else:
    print ("Opcion invalida...")
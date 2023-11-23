# Tarea 1 Algoritmos y Estructura de datos ---Carlos Perez---

print ( "---Programa que suma, resta, obtiene modulo y factorial de un numero---")

numero_uno = float ( input ("Ingrese un numero: "))
numero_dos = float ( input ("Ingrese un numero: "))

suma = numero_uno + numero_dos
resta = numero_uno + numero_dos
division = numero_uno / numero_dos
modulo = numero_uno % numero_dos

print ("El resultado de la suma es ",suma,"")
print ("El resultado de la resta es ",resta,"")
print ("El resultado de la modulo es ",division,"")
print ("El resultado de la modulo es ",modulo,"")


print ( "---Calculo de factorial de un numero---")

numero_tres = int (input ( "Ingrese un numero entero: "))

factorial = 1
for n in range (1,(numero_tres+1)):
    factorial = factorial * n
print ("El factorial de {0} es: {1}".format(numero_tres, factorial)) 
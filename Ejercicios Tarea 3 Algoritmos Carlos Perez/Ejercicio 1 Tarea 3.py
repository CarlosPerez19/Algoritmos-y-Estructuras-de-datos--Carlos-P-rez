#Carlos Perez
# Ejercicio Area y Perimetro

import math

pi = math.pi

print ("---Perimetro y area de un rectangulo---")

base = float (input ("Ingrese la base: "))
altura = float (input ("Ingrese la altura: "))

p1 = 2 * altura + 2 * base
a1 = base * altura

print ("El perimetro es ",p1,"")
print ("El area es ",a1,"")

print ("---Perimetro y area de un circulo---")

radio = float (input ("Ingrese el radio: "))

p2 = 2 * pi * radio
a2 =  pi * radio**2

print ("El perimetro es ",p2,"")
print ("El area es ",a2,"")
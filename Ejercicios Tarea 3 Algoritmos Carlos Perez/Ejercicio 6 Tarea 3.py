# Ejercicio Carlos Perez
# Ejercicio 6

from math import sqrt

x1 = float (input ("Ingresa el punto x1: "))
x2 = float (input ("Ingresa el punto x2: "))

y1 = float (input ("Ingresa el punto y1: "))
y2 = float (input ("Ingresa el punto y2: "))

distancia = sqrt ( (x1 - x2)**2 + (y1 - y2)**2 )

print ("La distancia entre puntos es: ",distancia,)
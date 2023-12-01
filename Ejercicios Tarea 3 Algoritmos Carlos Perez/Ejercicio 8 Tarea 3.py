# Ejercicio Carlos Perez
# Ejercicio 8

print ("---Recuerde que el auto 2 es mas veloz que el auto 1")

v1 = int (input ("Ingrese la velocidad del auto 1: "))
v2 = int (input ("Ingrese la velocidad del segundo auto: "))
distancia = float (input ("Ingrese la distancia a la que se encuentran los autos: "))

diferencia = v2 - v1
tiempo = distancia / diferencia 

tiempo = tiempo * 60

print ("Los autos se encuentran a ",tiempo, " minutos")

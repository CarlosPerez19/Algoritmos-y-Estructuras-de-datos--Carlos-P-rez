# Ejercicio Carlos Perez
suma = 0
numero = 1
contador = 0

while numero != 0:
   numero = float (input ("Ingrese un numero: "))
   suma = suma + numero
   contador += 1
   print (suma)
respuesta = suma / (contador - 1)
print (round(respuesta,2))
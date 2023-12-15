# Ejercicio Carlos Perez
# Contar pares e impares
pares = 0
impares = 0
contador = 0
numero = int (input ("Ingrese la cantidad de numeros que desea ingresar: "))

while contador < numero:
    num = int (input ("Ingrese un numero: "))
    if num % 2 == 0:
      pares = pares + 1
      
    else: 
      impares = impares + 1
    contador = contador + 1
    
print ("La cantidad de pares es de: ",pares)
print ("La cantidad de impares es de: ",impares)
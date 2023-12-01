# Ejercicio Carlos Perez 
# Ejercicio 15

precio = float (input ("Ingrese el precio de la uva: "))

print ("Seleccione el tipo de uva que desea")
print ("1. Tipo A")
print ("2. Tipo B")
uva = int (input ("Ingrese su seleccion: "))

print ("Seleccione el tamaño de la uva")
print ("1. Tamaño 1")
print ("2. Tamaño 2")
tamaño = int (input ("Ingrese su seleccion: "))

if uva == 1 and tamaño ==1:
    valor = (precio * 0.20)
    print ("El valor es: ",(precio + valor))

elif uva == 1 and tamaño ==2: 
    valor = (precio * 0.30)
    print ("El valor es: ",(precio + valor))
    
elif uva == 2 and tamaño == 1:
    valor2 = precio - (precio * 0.30)
    print ("Eñ valor es: ",valor2,)

elif uva == 2 and tamaño == 2:
    valor2 = precio - (precio * 0.50)
    print ("El valor es: ",valor2,)
    


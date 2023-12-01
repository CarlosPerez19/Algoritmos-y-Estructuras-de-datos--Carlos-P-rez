# Ejercicio Carlos Perez 
# Ejercicio 17

print ("---Bienvenido a nuestra aerolinea---")
print ("---Seleccione a donde quiere transportar el paquete---")
print ("1. America del Norte")
print ("2. America Central")
print ("3. America del Sur")
print ("4. Europa")
print ("5. Asia")

opcion = int (input ("Ingrese su seleccion: "))

peso = int (input ("Ingrese el peso de paquete en gramos: "))

if peso >= 5000:
    print ("Lo sentimos el paquete es muy pesado...")

elif opcion == 1:
    valor = peso * 24 
    print ("El costo es de ",valor,)

elif opcion == 2:
    valor = peso * 20 
    print ("El costo es de ",valor,)

elif opcion == 3:
    valor = peso * 21 
    print ("El costo es de ",valor,)

elif opcion == 4:
    valor = peso * 10 
    print ("El costo es de ",valor,)

elif opcion == 5:
    valor = peso * 18 
    print ("El costo es de ",valor,)

elif opcion > 5:
    print ("Opcion Invalida...")

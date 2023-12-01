# Ejercicio Carlos Perez 
# Ejercicio 16

alumnos = int (input ("Ingrese el numero de alumnos: "))

if alumnos >= 100: 
    costo = 65 * alumnos 
    pago = costo / alumnos
    print ("El pago a la compania es de: ",costo)
    print ("Los alumnos deben pagar un valor de: ",pago)

elif alumnos >= 50 and alumnos < 99:
    costo = 70 * alumnos 
    pago = costo / alumnos
    print ("El pago a la compania es de: ",costo)
    print ("Los alumnos deben pagar un valor de: ",pago)

elif alumnos >= 30 and alumnos < 49:
    costo = 95 * alumnos 
    pago = costo / alumnos
    print ("El pago a la compania es de: ",costo)
    print ("Los alumnos deben pagar un valor de: ",pago)

elif alumnos < 30:
    costo = 4000
    pago = costo / alumnos
    print ("El pago a la compania es de: ",costo)
    print ("Los alumnos deben pagar un valor de: ",pago)
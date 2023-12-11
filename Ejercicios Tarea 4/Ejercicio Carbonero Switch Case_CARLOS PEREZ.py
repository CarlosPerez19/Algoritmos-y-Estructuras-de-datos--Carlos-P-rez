# Ejercicio Carbonero Switch Case
# Carlos Perez

print ("---Bienvenido al Carbonero---")

print ("Ingrese los datos para su factura: ")
nombre =  input ("Ingrese su nombre: ")
cedula =  input ("Ingrese su numero de cedula: ")
corre =  input ("Ingrese su correo electronico: ")

print ("Las hamburguesas disponibles son: ")
print ("1. Sencilla   ----1.50$")
print ("2. Doble      ----2.50$")
print ("3. Triple     ----3.50$")
opcion = int (input ("Ingrese el numero de su seleccion: "))

match opcion:
    
    case 1:
        cantidad = int (input ("Ingrese la cantidad de hamburguesas que desea: "))
        pago = 1.50 * cantidad
        print ("Su total a pagar es de: ",pago)
        print ("Seleccione su metodo de pago: ")
        print ("1. Efectivo")
        print ("2. Tarjeta")
        opcion2 = int (input ("Ingrese el numero de su seleccion: "))
        match opcion2:
            case 1:
                print ("Usted no debe pagar cargo su total a pagar es de ",pago)
                print ("",nombre," Gracias por su compra")
                print ("La factura se enviara a su correo")
            case 2:
                cargo = pago + (pago * 0.5)
                print ("Su compra presenta un cargo de 5%: ",cargo)
                print ("",nombre," Gracias por su compra")
                print ("La factura se enviara a su correo")
            case other:
                print ("Seleccion Invalida...")

    case 2:
        cantidad = int (input ("Ingrese la cantidad de hamburguesas que desea: "))
        pago = 2.50 * cantidad
        print ("Su total a pagar es de: ",pago)
        print ("Seleccione su metodo de pago: ")
        print ("1. Efectivo")
        print ("2. Tarjeta")
        opcion2 = int (input ("Ingrese el numero de su seleccion: "))
        match opcion2:
            case 1:
                print ("Usted no debe pagar cargo su total a pagar es de ",pago)
                print ("",nombre," Gracias por su compra")
                print ("La factura se enviara a su correo")
            case 2:
                cargo = pago + (pago * 0.5)
                print ("Su compra presenta un cargo de 5%: ",cargo)
                print ("",nombre," Gracias por su compra")
                print ("La factura se enviara a su correo")
            case other:
                print ("Seleccion Invalida...")
    case 3:
        cantidad = int (input ("Ingrese la cantidad de hamburguesas que desea: "))
        pago = 3.50 * cantidad
        print ("Su total a pagar es de: ",pago)
        print ("Seleccione su metodo de pago: ")
        print ("1. Efectivo")
        print ("2. Tarjeta")
        opcion2 = int (input ("Ingrese el numero de su seleccion: "))
        match opcion2:
            case 1:
                print ("Usted no debe pagar cargo su total a pagar es de ",pago)
                print ("",nombre," Gracias por su compra")
                print ("La factura se enviara a su correo")
            case 2:
                cargo = pago + (pago * 0.5)
                print ("Su compra presenta un cargo de 5%: ",cargo)
                print ("",nombre," Gracias por su compra")
                print ("La factura se enviara a su correo")
            case other:
                print ("Seleccion Invalida...")
    case other:
        print ("Seleccion invalida...")
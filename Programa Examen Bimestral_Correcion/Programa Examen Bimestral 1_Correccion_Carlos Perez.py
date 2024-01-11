# Prueba examen Python Carlos Perez

correo = "tosh@gmail.com"
contraseña = "Secret*"

correo_ingresado = input ("Ingrese su correo electronico: ")
contraseña_ingresada = input ("Ingrese su contraseña: ")
while correo_ingresado != correo or contraseña_ingresada != contraseña:
    print ("---ERROR---\n Correo o contraseña ingresados incorrectos")
    correo_ingresado = input ("Ingrese su correo electronico: ")
    contraseña_ingresada = input ("Ingrese su contraseña: ")

seleccion = 0

while seleccion != 3:
    print ("---Bienvenido a Amazon---")
    print ("1. Ingresar productos al carrito de compras \n2. Facturar \n3. Salir")
    seleccion = int (input ("Ingrese el numero de su seleccion: "))

    if seleccion == 1:
        print ("---Carrito de compra---")
        numero_De_productos = int (input ("Ingrese el numero de productos adquiridos: "))
        contador_productos = 1
        productos_con_descuento = 0
        suma_productos = 0

        while contador_productos <= numero_De_productos:

            descuento = input ("¿El producto tiene cupon de descuento?: (si/no): ")     # Carlos Perez
            if descuento != "Si" and descuento != "si":
               precio = float (input ("Ingrese el precio del producto: "))
               while precio < 0:
                   print ("El precio del producto no puede ser negativo")
                   precio = float (input ("Ingrese el precio del producto: "))
               suma_productos = suma_productos + precio
            else:
                codigo_descuento = input ("Ingrese el codigo de descuento: ")

                if codigo_descuento != "Enero" and codigo_descuento != "enero":
                    print ("No aplica al descuento")
                    precio = float (input ("Ingrese el precio del producto: "))
                    while precio < 0:
                      print ("El precio del producto no puede ser negativo")
                      precio = float (input ("Ingrese el precio del producto: "))
                    suma_productos = suma_productos + precio
                else: 
                    precio = float (input ("Ingrese el precio del producto: "))
                    while precio < 0:
                     print ("El precio del producto no puede ser negativo")
                     precio = float (input ("Ingrese el precio del producto: "))
                    suma_productos = suma_productos + precio - (precio * 0.15)
                    precio_con_descuento = suma_productos
                    productos_con_descuento = productos_con_descuento + 1
            contador_productos = contador_productos + 1

    elif seleccion == 2:
        print ("---Factura Electronica---")
        print ("La factura se enviara a su correo")
        print ("---Descuento---")
        print ("*Detalle del cupon de descuento")
        if descuento != "si" and descuento != "Si":  # Carlos Perez
            print ("*No se utilizo codigo descuento (en todos o en uno de sus articulos)")
        else:
            if codigo_descuento != "Enero" and codigo_descuento != "enero":     
              print ("*No aplica a descuento (en todos o en uno de sus articulos)")
            else:
             print ("*Nombre del cupon de descuento es: ",codigo_descuento,)
        print ("*El numero de productos con descuento son: ",productos_con_descuento)
        print ("El precio de final de su producto/s con descuento es: ", precio_con_descuento )
        print ("*El precio de la factura final es de: ",suma_productos)
    
        
    elif seleccion == 3:
        print ("Gracias por utilizar nuestro sistema :D") # Carlos Perez

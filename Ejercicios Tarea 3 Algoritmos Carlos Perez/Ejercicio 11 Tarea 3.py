# Ejercicio Carlos Perez 
# Ejercicio 11

n = input("Introduzca una letra: ")

if n == n.lower():

    if n in ("a","e","i","o","u"):
       print ("Es minuscula y una vocal")
    else:
        print ("Es minuscula y una consonante")
else:
    if n in ("A","E","I","O","U"):
       print ("Es mayuscula y una vocal")
    else:
     print ("Es mayuscula y una consonante")
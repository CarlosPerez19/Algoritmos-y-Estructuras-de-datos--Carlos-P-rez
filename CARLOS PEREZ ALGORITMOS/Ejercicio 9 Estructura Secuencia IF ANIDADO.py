# Ejercicio Carlos Perez

nota1 = float (input (" Ingrese la nota de Base de datos: "))
nota2 = float (input (" Ingrese la nota de Programacion: "))
nota3 = float (input (" Ingrese la nota de Matematica: "))

promedio = (nota1 + nota2 + nota3) / 3

print ("Su promedio es de",promedio,"")

if promedio >= 9 and promedio <= 10:
    print ("Usted aprobo el curso y ha obtenido una beca")
    if promedio >= 7 and promedio <=8:
        print ("Felicidades aprobo la materia")
    else: 
        print ("Usted reprobo la materia")
else:
   print ("Las notas estan fuera de rango")

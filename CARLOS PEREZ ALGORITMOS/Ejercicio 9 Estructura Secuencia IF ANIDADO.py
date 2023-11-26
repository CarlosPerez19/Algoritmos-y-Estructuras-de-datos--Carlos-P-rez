# Ejercicio Carlos Perez

nota1 = float (input (" Ingrese la nota de Base de datos: "))
nota2 = float (input (" Ingrese la nota de Programacion: "))
nota3 = float (input (" Ingrese la nota de Matematica: "))

promedio = (nota1 + nota2 + nota3) / 3


if promedio >= 9 and promedio <= 10:
    print ("Usted aprobo el curso y ha obtenido una beca su promedio es de ",round (promedio,2),"")
elif promedio >= 7 and promedio <= 8:
    print ( "Usted aprobo el curso su promedio es de ",round(promedio,2),"")
elif promedio < 7:
    print ("Usted reprobo la materia su promedio es de ",round(promedio,2),"")
else: 
    print ("Las notas estan fuera de rango")

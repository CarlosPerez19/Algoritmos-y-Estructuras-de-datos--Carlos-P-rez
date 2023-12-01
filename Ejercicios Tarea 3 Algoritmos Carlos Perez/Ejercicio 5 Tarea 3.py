# Ejercicio Carlos Perez
# Ejercicio 5

print ("---Calificaciones finales algoritmos---")

nota1 = float (input ("Ingresa tu primera nota parcial: "))
nota2 = float (input ("Ingresa tu segunda nota parcial: "))
nota3 = float (input ("Ingresa tu tercera nota parcial: "))

nota4 = float (input ("Ingresa la nota de tu examen final: "))

nota5 = float (input ("Ingresa la nota de tu trabajo final: "))

promedio = ((nota1 + nota2 + nota3)/3) * 0.55
promedio2 = (nota4) * 0.30
promedio3 = (nota5) * 0.15

promedio_final = promedio + promedio2 + promedio3

print ("Tu promedio parcial es: ",promedio,)
print ("Tu nota de examen final es: ",promedio2,)
print ("Tu nota de trabajo final es: ",promedio3,)
print ("Tu promedio final es: ",promedio_final,)
# Ejercicio Carlos Perez
# Ejercicio 19

alumno = input ("Ingrese su nombre: ")
nota = float (input ("Ingrese su nota de Ingles: "))

if nota >= 9 and nota <= 10:
    print ("Felicitaciones su nota es ",nota," equivalente a excelente")

elif nota >= 7 and nota <= 8:
     print ("Siga adelante su nota es ",nota," equivalente a muy buena")

elif nota >= 5 and nota <= 6:
     print ("Debe esforzarse más su nota es ",nota," equivalente a buena")
     
elif nota > 0 and nota <= 4:
     print ("usted puede reprobar ya que su nota es ",nota," equivalente a regular")
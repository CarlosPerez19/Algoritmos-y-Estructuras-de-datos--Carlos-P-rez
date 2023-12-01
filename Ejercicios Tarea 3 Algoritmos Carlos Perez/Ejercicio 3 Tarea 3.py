#Carlos Perez
# Ejercicio Transformacion a horas y minutos

minutos = int (input ("Ingresa la cantidad de minutos: "))

horas = minutos / 60
res_minutos = minutos % 60

print ("El tiempo es ",horas," horas y ",res_minutos," minutos")
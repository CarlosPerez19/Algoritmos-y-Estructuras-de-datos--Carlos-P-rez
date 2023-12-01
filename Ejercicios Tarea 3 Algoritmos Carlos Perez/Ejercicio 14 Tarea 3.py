# Ejercicio Carlos Perez 
# Ejercicio 14

def tipo_de_triangulo(A, B, C):

    if A**2 + B**2 == C**2 or B**2 + C**2 == A**2 or A**2 + C**2 == B**2:
        return "Triángulo rectángulo"
    
    elif A == B or B == C or A == C:
        return "Triángulo isósceles"
    
    elif A == B == C:
        return "Triángulo equilátero"
    
    else:
        return "Triángulo escaleno"

A = float(input("Ingrese la longitud del lado A: "))
B = float(input("Ingrese la longitud del lado B: "))
C = float(input("Ingrese la longitud del lado C: "))

resultado = tipo_de_triangulo(A, B, C)
print("El triángulo es: ",resultado,"")
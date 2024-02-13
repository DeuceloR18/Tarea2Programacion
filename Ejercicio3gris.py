"""Por medio del algoritmo de euclides calcular el mcd de 24 & 62"""
print("1. primero debemos dividir el numero mas grande entre el mas pequeño por lo que dividimos 62 entre 24 y el cociente es 2 y el residuo 14")
print("2. dividimos 24 entre 14, el cociente es 1 y el residuo 10")
print("3. luego dividimos 14 entre 10, el cociente es 1 y el resido es 4")
print("4. luego dividimos 10 entre 4, el cociente es 2 y residuo es 2")
print("5. luego dividimos 4 entre 2 el cociente es 2 y el residuo 0")



def euclides(num1,num2,iteracciones=1):
    if num1<num2:
        num1,num2=num2,num1
    resto=num1%num2
    if resto==0:
        return (num2,iteracciones)
 
    #llamamos nuevamente a la función pasando como primer parametro el segundo numero y el resto de la division'''
    return euclides(num2,resto,iteracciones+1)
 
#Almacenamos los valores de num1 y num2

num1=24
num2=62
 
comunDivisor,iteracciones=euclides(num1,num2)
 # Pedimos que muestre los resultados al usuario.

print("El MCD de {} y {} es ={}".format(num1,num2,comunDivisor))


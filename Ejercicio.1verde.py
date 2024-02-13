#Calcular placas de vehiculos
print("Para calcular el numero de placas debemos considerar los valores de numeros y letras permitidos en este caso hay 27 letras y 10 numeros")
print("Para formar una placa se deben tomar 3 numeros y 3 letras ")
print("se puede usar la formula de permutacion que es n!/(n-r)")
print("Donde n es el número total de elementos en el conjunto y r es el número de elementos que se seleccionan para formar la permutación.")
import math
#Almacenamos los valores de los numeros y letras
total_numeros = 10
total_letras = 27
#se deben seleccionar 3 numeros y 3 letras para formar una placas
placas = math.perm(total_numeros, 3) * math.perm(total_letras, 3)
'''Pedimos que imprima el resultado'''
print("El numero de placas que se puede emitir en Guatemala es",placas)
import math
#Almacenamos los valores de los numeros y letras
total_numeros = 10
total_letras = 27
#se deben seleccionar 3 numeros y 3 letras para formar una placas
placas = math.perm(total_numeros, 3) * math.perm(total_letras, 3)
'''Pedimos que imprima el resultado'''
print("El numero de placas que se puede emitir en Guatemala es",placas)
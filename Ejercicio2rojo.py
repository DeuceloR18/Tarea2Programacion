print("1.Calcular el conjunto resultante, de la interseccion de los conjuntos que estan conformados por los conjuntos A y B primero debemos conocer los elementos de cada conjunto")
print("2.Con el tipo set permite almacenar los elementos y que no pueden haber elementos duplicados")
print("3Luego el resultado conjunto resultante es donde se toman los elementos mas comunes de A y B")
import datetime
mes_actual = datetime.datetime.now().strftime("%B")
conjunto_a = set("septiembre")
# Conjunto B

conjunto_b = set("abcdefghij")
conjunto_resultante = conjunto_a & conjunto_b
'''Pedimos que imprima el resultado al usuario con el conjunto resultante'''
print(conjunto_resultante)
print("resultado")
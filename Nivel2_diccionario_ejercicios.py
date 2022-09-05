# -*- coding: utf-8 -*-
"""
1.Construya un diccionario con las alturas sobre el nivel del mar de las capitales
de los países suramericanos. Use los nombres de las ciudades, usando mayúsculas
al principio de las palabras, como llaves y las alturas como valores. Es decir,
las llaves deben ser ‘Bogotá’, ‘Buenos Aires’. etc.
"""
Altura_nivel_mar = { 'Bogota' : 2.630,
             'Buenos Aires' : 25, 
             'Brasilia' : 1.172,
             'Santiago de Chile' : 570}

"""
2.Escriba una función que reciba el diccionario con las alturas de las ciudades
y los nombres de dos ciudades y que retorne el nombre de la ciudad que esté
ubicada a una mayor altura. La función debe ser capaz de funcionar incluso si
en el nombre de las ciudades se usan mayúsculas y minúsculas de forma diferente
a como están en el diccionario (por ejemplo, ‘BoGoTá’ y ‘BUENOS aires’). Si
alguno de los dos nombres no corresponde a una ciudad, la función debe retornar
el valor None.
"""
def ciudad_mayor_altura(diccionario: dict, ciudad1: str, ciudad2: str):
    ciudad_1 = ciudad1.title()
    ciudad_2 = ciudad2.title()
    altura_ciudad1 = Altura_nivel_mar.get(ciudad_1, None)
    altura_ciudad2 = Altura_nivel_mar.get(ciudad_2, None)
    if altura_ciudad1 and altura_ciudad2 is not None:
        if altura_ciudad1 > altura_ciudad2:
            return ciudad1
        if altura_ciudad2 > altura_ciudad1:
            return ciudad2
        else: 
            print('ambas ciudades estan a la misma altura')
        
ciudad1 = 'BogotA'
ciudad2 = 'Brasilia'
diccionario = Altura_nivel_mar
funcion_ciudad_mas_alta = ciudad_mayor_altura(diccionario, ciudad1, ciudad2)
print(funcion_ciudad_mas_alta)

"""
4.Escriba una función que reciba un número entero y retorne el dígito que aparece
más veces dentro del número.
"""
def numero_frecuencia(numero_entero: int):
#preguntar a jorge 
    
"""
5. Con base en el ejemplo del diccionario de celulares, construya una función
que reciba los diccionarios de 4 celulares y cuente cuántos de estos celulares
tienen más de 16 GB de memoria.
"""

def celulares_buena_memoria(memoria_celulares: dict) -> None:
    for k,v in memoria_celulares.items():
        if v > 14:
            return memoria_celulares.counter()
            
memoria_celulares = {'Xiaomi': 16, 'Motorola': 14, 'Iphone': 20, 'Redmi': 18}
celulares_memoria_16g = celulares_buena_memoria(memoria_celulares)
print(celulares_memoria_16g)
#preguntar a jorge 
"""
6.Con base en el ejemplo del diccionario de celulares, construya una función que
reciba los diccionarios de 4 celulares y diga cuál es el celular que tiene la
mayor cantidad de pixeles en la pantalla.
"""
def celulares_mas_pixeles(pixeles_celulares: dict) -> None:
    for k,v in pixeles_celulares.items():
        if max(v):
            return k
            
pixeles_celulares = {'Xiaomi': 1200, 'Motorola': 1400, 'Iphone': 2099, 'Redmi': 1800}
celulares_con_mas_pixeles = celulares_mas_pixeles(pixeles_celulares)
print(celulares_con_mas_pixeles)
#preguntar a jorge 
"""
7.Con base en el ejemplo del diccionario de celulares, construya una función que
reciba los diccionarios de 4 celulares y los modifique para duplicar la
capacidad de la pila de todos.
"""
"""
8.Modifique el programa que calcula cuáles valores salieron en los lanzamientos
de 6 dados para que ahora calcule un histograma en el que se pueda saber cuántas
veces salió cada número.
"""

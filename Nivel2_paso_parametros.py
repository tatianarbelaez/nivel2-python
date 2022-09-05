# -*- coding: utf-8 -*-
"""
Para empezar, vamos a recoerdar la diferencia entre el operador == y el operador
is: el primero lo podemos usar para comparar los valores de unas variables para
ver si son iguales, mientras que el segundo nos sirve para saber sin son el mismo.
"""
d1 = {"k1" : 1}
d2 = {"k1" : 1}
d1 == d2 #es True porque tienen la misma llave y valores
d1 is d2 #es False porque son variables distintas a pesar de tener el mismo contenido.

"""
Parametro por valor y referencia
Un parámetro se pasa por valor, cuando el valor se copia para que se utilice
dentro de la función. Esto es lo que ocurre con algunos tipos básicos como int,
float y bool, y también con tipos inmutables como str y tuple.

Por otro lado, un parámetro se pasa por referencia, cuando lo que se hace es
entregarle a la función una referencia al elemento, sin copiarlo 1 . Esto quiere
decir que si la función hace cambios al elemento, esos cambios los podrá ver
quien haya invocado a la función. Esto va a ocurrir en Python con tipos de datos
como los diccionarios
"""
def limpiar_diccionario(el_diccionario: dict) -> None:
    el_diccionario.clear()
    
d = {"a":1, "b":2, "c": 3}
print(d)
limpiar_diccionario(d)
print(d)

"""
IMPORTANTE
Los tipos básicos como int, float y bool, y los inmutables como str y tuple se
comportan como si se pasaran por valor.

Los tipos complejos y mutables como dict y list se comportan como si se pasaran
por referencia.
"""

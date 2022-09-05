# -*- coding: utf-8 -*-
"""
DICCIONARIO 
Un diccionario es una estructura de datos que contiene muchos valores, 
identificados cada uno con una llave que es única.
"""
palabras = { 'imagen' : 'Figura, representación, semejanza y apariencia de algo',
             'figura' : 'Forma exterior de alguien o de algo', 
             'baraja' : 'Conjunto completo de cartas empleado para juegos de azar',
             'posibilidad' : 'Aptitud, potencia u ocasión para ser o existir algo' }
type(palabras) #un diccionario es tipo dict
len(palabras)  #al sacarle  la longitud me sale el numero de parejas 

definicion_imagen = palabras['imagen']
print(definicion_imagen)

llave = 'IMAGEN'
# Preguntar si la llave está en el diccionario antes de consultar
if llave in palabras:
  definicion = palabras[llave]
else:
  definicion = "La palabra '" + llave + "' no se encuentra en el diccionario"
"""
Aunque no está prohibido en el lenguaje, es recomendable evitar tener llaves 
de diferentes tipos en el mismo diccionario (algunas numéricas, otras cadenas,
                                             otras booleanas, etc.).

"""
diccionario = {"llave":"valor", "palabra":"definición"}
llave = "llave"
print("1.", diccionario["llave"])
print("2.", diccionario[llave])
llave = "palabra"
print("3.", diccionario[llave])
print("4.", diccionario["palabra"])
print("5.", diccionario[palabra]) #error no hemos definido variable palabra 

"""
*Metodo get 
Este método, que se aplica sobre un diccionario, recibe como parámetros una
llave y el valor que se debería retornar si la llave no existe en el
diccionario.
"""
llave = 'IMAGEN'
definicion = palabras.get(llave, "La palabra '" + llave + "' no se encuentra en el diccionario")
print(definicion)

"""
*Valor none
El valor None, que se puede traducir como ninguno, es un valor que se usa en
Python para denotar la “ausencia de un valor”
"""
import math
def solucionar_cuadratica(a: int, b: int, c:int) -> tuple:
    """ Encuentra las soluciones reales de una ecuación cuadrática de la forma
        y = ax^2 + bx + c
    Parámetros:
      a (int): El coeficiente del término de orden 2
      b (int): El coeficiente del término de orden 1
      c (int): El coeficiente del término de orden 0
    Retorna:
      (tuple): Una tupla con las soluciones reales de la ecuación.
               Retorna None si la ecuación no tiene solución real.
    """
    soluciones = None
    determinante = (b**2) - (4*a*c)
    if determinante >= 0:
        sol1 = -b + (math.sqrt(determinante))
        sol2 = -b - (math.sqrt(determinante))
        soluciones = (sol1, sol2)
    return soluciones

def imprimir_soluciones(soluciones: tuple) -> None:
    """ Imprime las soluciones de una ecuación cuadrática o imprime
        un mensaje indicando que no había soluciones.
    Parámetros:
      soluciones (tuple): Una tupla con dos elementos que son las soluciones de la ecuación.
                          Si no hay soluciones reales, 'soluciones' debe tener el valor None.
    """
    if soluciones is None:
        print("La ecuación no tenía soluciones reales")
    else:
        print("Las soluciones son", soluciones[0], "y", soluciones[1])

# Calcular e imprimir las soluciones de una ecuación sin soluciones reales
soluciones = solucionar_cuadratica(1,1,1)
imprimir_soluciones(soluciones)

# Calcular e imprimir las soluciones de una ecuación con dos soluciones reales diferentes
soluciones = solucionar_cuadratica(1,0,-1)
imprimir_soluciones(soluciones)

"""
La explicación anterior sobre el valor None es relevante porque se usa muy
frecuentemente con el método get: si una llave no se encuentra en un diccionario,
usar None como valor por defecto es lo más natural en muchos casos y es mucho
mejor que usar cosas como cadenas vacías o sólo con espacios. 
"""
def imprimir_definicion(diccionario: dict, palabra: str) -> None:
    """ Imprime la definición de una palabra o, si la palabra no existe,
        un mensaje indicando el problema.
    Parámetros:
      diccionario (dict): Un diccionario con las palabras y sus definiciones
      palabra (str): La palabra para la que se quiere la definición
    """
    definicion = palabras.get(palabra, None)
    if definicion is not None:
         print("La definición de", palabra, "es:", definicion)
    else:
         print("La palabra '" + llave + "' no se encuentra en el diccionario")

"""
*Modificar diccionario
Esta primera versión de la función muestra cómo se modifica un diccionario:
usando la misma convención que para consultar (paréntesis cuadrados alrededo
del nombre de la llave), le asignamos una definición a la palabra. Veamos
ahora cómo invocar la nueva función:
"""         
def agregar_definicion(diccionario: dict, palabra: str, definicion: str)-> None:
  diccionario[palabra] = definicion
  
palabras = {}
agregar_definicion(palabras, 'imagen', 'Figura, representación, semejanza y apariencia de algo')
agregar_definicion(palabras, 'figura', 'Forma exterior de alguien o de algo')

"""
La última operación para estudiar es la que nos permite eliminar definiciones 
de un diccionario. Esto se puede lograr de dos formas: con el operador del o
con el método pop. Tenga en cuenta que en ambos casos es necesario verificar
que la llave exista en el diccionario antes de intentar eliminarla. De lo
contrario se producirá un error.
"""
def eliminar_palabra(diccionario: dict, palabra: str)-> bool:
    palabra_eliminada = False
    if palabra in diccionario:
        del diccionario[palabra]
        palabra_eliminada = True
    return palabra_eliminada

palabras = {}
agregar_definicion(palabras, 'imagen', 'Figura, representación, semejanza y apariencia de algo')
agregar_definicion(palabras, 'toballa', 'Toalla')
agregar_definicion(palabras, 'toballa', 'Pieza de felpa')
res1 = eliminar_palabra(palabras, 'caracter')
res2 = eliminar_palabra(palabras, 'toballa')
print(res1, res2)
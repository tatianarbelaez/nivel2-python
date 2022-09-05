# -*- coding: utf-8 -*-
"""
MODULO MATH

* gcd(x, y): función para calcular el máximo común divisor de dos números 
(Gratest Common Denominator).

*log(x, base): función para calcular el logaritmo de un número con respecto a
una base.

*log2(x): función para calcular el logaritmo de un número en base 2.

*sqrt: función para calcular la raíz cuadrada de un número.

π --> math.pi

e (número de Euler)--> math.e

inf, el valor que utiliza Python para representar el infinito.--> math.inf

nan, el valor que utiliza Python para representar un número indefinido--> math.nan
"""
import math 

print("El valor de pi:", math.pi)

print("El valor de e:", math.e)

print("El valor de infinito:", math.inf)

print("El valor de un número indefinido:", math.nan)

"""
MODULO RANDOM

random.random() -->generar valores uniformemente distribuidos entre 0 y 1
random.uniform()-->recibe dos parámetros ‘a’ y ‘b’ y genera un número aleatorio
en el intervalo [a, b).
random.randit()-->generar valores enteros entre dos números ‘a’ y ‘b’
random.normalvariate -->genera números distribuidos de acuerdo a una 
distribución normal.Esta función requiere de un parámetro mu (el valor promedio 
de los valores en la distribución) y de un parámetro sigma (la desviación 
estándar de los valores) para generar valores que se distribuyan de forma normal de acuerdo con los parámetros.
"""
import random

lanzamiento = random.randint(1, 12)
valor = random.random() * 5
numero = random.randrange(12, 20, 2)
random.normalvariate(10,1.5)

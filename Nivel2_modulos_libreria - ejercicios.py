# -*- coding: utf-8 -*-
"""
Usando la función random.normalvariate genere 15 números aleatorios con media
3.8 y desviación estándar de 1. Calcule ahora usted la media de los números
generados y la desviación estándar. ¿Qué tan lejos están de la media y la
desviación planeada? Ejecute su programa y observe cómo cambian los resultados
con cada ejecución.
"""
import random 
import itertools

numero = random.normalvariate(3.8, 1)
aleatoria_normal = itertools.repeat(numero, 15)
print(aleatoria_normal)

# -*- coding: utf-8 -*-
"""
1.Vamos a representar a un estudiante usando un diccionario con 4 llaves: "nombre",
para almacenar su nombre; y "matemáticas", "lenguaje" y "ciencias" para almacenar
las notas en cada una de las 3 materias. Escriba una función que reciba un
estudiante (un diccionario) y retorne su promedio.
"""
def promedio_estudiante(diccionario_estudiante: dict):
    nota_matematicas = diccionario_estudiante.get('matematicas')
    nota_lenguaje = diccionario_estudiante.get('lenguaje')
    nota_ciencias = diccionario_estudiante.get('ciencias')
    promedio = (nota_matematicas + nota_lenguaje + nota_ciencias)/3
    return promedio 
diccionario_estudiante = {'nombre': 'Santiago', 'matematicas': 3, 'lenguaje': 5, 'ciencias': 4}
calcular_promedio_estudiante = promedio_estudiante(diccionario_estudiante)
print(calcular_promedio_estudiante)

"""
2. Ahora escriba una función que reciba un estudiante (un diccionario), el nombre
de una de las tres materias, y una nota, y le asigne al estudiante la nueva nota
en esa materia.
"""
def asignar_nota(diccionario_estudiante: dict, materia: str, nota: int):
    diccionario_estudiante[materia] = nota
    return diccionario_estudiante
materia = 'lenguaje'
nota = 2
nueva_nota = asignar_nota(diccionario_estudiante, materia, nota)
print(nueva_nota)
    
"""
3. Escriba una función que reciba tres estudiantes (tres diccionarios) y el nombre
de una de las tres materias. La función debe aumentar la nota de cada estudiante
en la materia en un 10% del promedio de los tres estudiantes en esa materia.
"""
def aumentar_nota(diccionario_estudiante: dict, diccionario_estudiante2: dict, diccionario_estudiante3: dict, materia: str):
    promedio_materia = (diccionario_estudiante[materia] + diccionario_estudiante2[materia] + diccionario_estudiante3[materia])/3
    diccionario_estudiante[materia] += promedio_materia * 0.1
    diccionario_estudiante2[materia] += promedio_materia * 0.1
    diccionario_estudiante3[materia] += promedio_materia * 0.1
    return diccionario_estudiante[materia], diccionario_estudiante2[materia], diccionario_estudiante3[materia]
diccionario_estudiante2 = {'nombre': 'Tatiana', 'matematicas': 5, 'lenguaje': 4, 'ciencias': 3}
diccionario_estudiante3 = {'nombre': 'Jorge', 'matematicas': 4, 'lenguaje': 3, 'ciencias': 5}
calcular_aumento_nota = aumentar_nota(diccionario_estudiante, diccionario_estudiante2, diccionario_estudiante3, materia)
print(calcular_aumento_nota)

"******************************************************************************"
"""
1. Construya una función que reciba dos números enteros como parámetros: si el
primer número es par, la función debe retornar la suma de los dos números; de lo
contrario, debe retornar la multiplicación de los dos números.
"""
def suma_o_multiplicacion(numeros: tuple):
    if numeros[0] % 2 == 0:
        return numeros[0] + numeros[1]
    else: 
        return numeros[0] * numeros[1]
numeros = (8, 3)
calcular_suma_o_multiplicacion = suma_o_multiplicacion(numeros)
print(calcular_suma_o_multiplicacion)
"""
2.Invoque su función con varias parejas de números igual que como lo ha estado
haciendo hasta el momento.
"""
numeros = (4, 17)
calcular_suma_o_multiplicacion = suma_o_multiplicacion(numeros)
print(calcular_suma_o_multiplicacion)

numeros = (13, 5)
calcular_suma_o_multiplicacion = suma_o_multiplicacion(numeros)
print(calcular_suma_o_multiplicacion)
"""

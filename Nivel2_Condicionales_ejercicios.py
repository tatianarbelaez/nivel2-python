# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 17:59:54 2021

@author: user
"""
"""
Modifique el programa que cambia la contraseña para que en caso de que no se
pueda cambiar la contraseña se le informe al usuario no sólo las restricciones
que no se cumplieron sino también las condiciones que sí se cumplieron.
"""
contrasena_anterior = 'tati1223'
nueva = input("Introduzca su nueva contraseña:")
contrasena_correcta = True
mensaje = ""

if len(nueva) < 8:
    contrasena_correcta = False
    mensaje += "La nueva contraseña debe tener al menos 8 caracteres" + "\n"
else:
    mensaje += "la nueva contraseña tiene al menos 8 caracteres" + "\n"
    
if nueva == contrasena_anterior:
    contrasena_correcta = False
    mensaje += "La nueva contraseña no puede ser igual a la anterior" + "\n"
else:
    mensaje += "La nueva contraseña no es igual a la anterior" + "\n"

if nueva.isalnum():
    contrasena_correcta = False
    mensaje += "La nueva contraseña debe tener signos de puntuación" + "\n"
else: 
    mensaje += "La nueva contraseña tiene signos de puntuación" + "\n"

print(mensaje)

"""
El valor de un peaje depende del tipo de vehículo (categoría) que pase y de la
cantidad de ejes que tenga: automóviles, camionetas y camperos (AUTO) deben
pagar 10000; buses y busetas (BUS), 14300; camiones grandes de 2 ejes (CAMION),
16000; camiones de 3 y 4 ejes (CAMION), 28100; camiones de 5 ejes (CAMION), 
37700; y camiones de 6 o más ejes (CAMION) deben pagar 41400. Adicionalmente,
un vehículo podría tener un descuento especial del 15% por paso frecuente. 
Escriba una función que reciba el tipo de un vehículo (‘AUTO’, ‘BUS’ o ‘CAMION’) 
y si tiene descuento especial y calcule el valor que debe pagar en el peaje.
"""

def peaje(categoria, frecuente):
    if categoria == 'AUTO':
        precio_categoria = 10000
    elif categoria == 'BUS':
        precio_categoria = 14300
    elif categoria == 'CAMION':
        ejes = int(input("Si su vehiculo es CAMION cuantos ejes tiene? (1, 2, 3, 4...NA) "))
        if ejes == 2:
            precio_categoria = 16000
        elif ejes == 3 or ejes == 4:
            precio_categoria = 28100
        elif ejes == 5:
            precio_categoria = 37700
        elif ejes > 6:
            precio_categoria = 41400
        else:
            print ("no es posible ese numero de ejes")
            exit(1)
    else:
        print("no es posible ese tipo de vehiculo")
        exit(1)
    
    precio_peaje = 0 
    if (frecuente == 'S' or frecuente == 's' or frecuente == 'si'):
        precio_peaje = 0.85 * precio_categoria
    elif (frecuente == 'N' or frecuente == 'n' or frecuente == 'no'):
        precio_peaje = precio_categoria
    else:
        print("no es posible ese tipo de paso frecuente")
        exit(1)
    return precio_peaje

categoria = input("introduzca el tipo de vehiculo(AUTO, BUS, CAMION): ")
frecuente = input("pasa frecuentemente por este peaje?(S, N) ")

valor_peaje = peaje(categoria, frecuente)
print(valor_peaje)

"""    
Escriba una función que reciba por parámetro cuatro números enteros y devuelva 
el mayor de estos. Si hay dos o más iguales y mayores, retorna cualquiera de estos.
La signatura de la función debe ser:  
"""
def mayor(a: int, b: int, c:int, d:int)->int:
    if (a >= b) and (a >= c) and (a >= d):
        num_mayor = a 
    elif (b >= a) and (b >= c) and (b >= d):
        num_mayor = b 
    elif (c >= a) and (c >= b) and (c >= d):
        num_mayor = c 
    else:
        num_mayor = d 
    
    return num_mayor 

a = 5
b = 3
c = 10
d = 8
numero_mayor = mayor(a, b, c, d)
print(numero_mayor)

""" 
Modifique el ejercicio que retorna el número mayor para que retorne el número 
del parámetro en el que se encuentra el número mayor. Si hay dos o más iguales 
y mayores, debe retornar el número de parámetro menor (ej. si el primer y el 
tercer parámetro eran los mayores, debe retornar el número 1).
""" 
def mayor(a: int, b: int, c:int, d:int)->int:
    if (a >= b) and (a >= c) and (a >= d):
        num_mayor = a 
    elif (b >= a) and (b >= c) and (b >= d):
        num_mayor = b 
    elif (c >= a) and (c >= b) and (c >= d):
        num_mayor = c 
    else:
        num_mayor = d 
    
    return (num_mayor)

a = 5
b = 3
c = 10
d = 8
numero_mayor = mayor(a, b, c, d)
print(numero_mayor)
#PREGUNTAR A JORGE

""" 
La calificación final de un estudiante en un curso depende de las calificaciones
que obtenga en 3 exámenes, pero con unas reglas especiales. Si el estudiante 
sacó más de 4.0 sobre 5.00 en el tercer examen (el examen final), la nota en el
curso será la nota del examen final. Si el estudiante saca menos de 2.0 en el
examen final, ese examen valdrá el 50% de la nota y los otros dos exámenes 
valdrán el 25% cada uno. En cualquier otro caso, los exámenes pesarán lo mismo
para calcular la nota final. Escriba una función que dadas las notas de los tres
exámenes calcule la nota del estudiante en el curso.
""" 
def nota_final(examen1, examen2, examen_final):
    if examen_final >= 4:
        nota_curso = examen_final
    elif examen_final < 2:
        nota_curso = 0.5  * examen_final + 0.25 * (examen1 + examen2)
    else:
        nota_curso = (examen1 + examen2 + examen_final)/3
    return nota_curso

examen1 = 3.8
examen2 = 4.7
examen_final = 3.5

calificacion_final_curso = nota_final(examen1, examen2, examen_final)
print(calificacion_final_curso)

""" 
En muchos torneos de fútbol es usual que dos equipos jueguen dos partidos para 
definir cuál es el mejor de ellos: uno en el estadio del primer equipo y otro 
en el estadio del segundo equipo. También es usual que, en caso de empate en la
cantidad de partidos ganados, los goles de los equipos visitantes cuenten por
dos al momento de calcular la diferencia de goles. Escriba una función para 
calcular el ganador entre dos equipos. La función debe recibir el nombre del 
primer equipo (A), el nombre del segundo equipo (B), los goles que hizo A de
local, los goles que hizo B de visitante, los goles que hizo A de visitante y 
los goles que hizo B de local. La función debe retornar el nombre del ganador 
de la serie o la cadena “EMPATE” si hubo un empate entre los equipos.
""" 
def ganador_final(equipoA, equipoB, goles_localA, goles_visA, goles_localB, goles_visB):
    goles_totalA = goles_localA + goles_visA
    goles_totalB = goles_localB + goles_visB
    if goles_totalA != goles_totalB:
        if goles_totalA > goles_totalB:
            ganador = equipoA
        else:
            ganador = equipoB
    elif goles_totalA == goles_totalB:
        if 2 * goles_visA + goles_localA > 2 * goles_visB + goles_localB:
            ganador = equipoA
        else:
            ganador = equipoB
        return ganador 
    
equipoA = 'Bogota'
equipoB = 'Cali'
goles_localA = 2
goles_visA = 1
goles_localB = 1
goles_visB = 2

Ganador_torneo = ganador_final(equipoA, equipoB, goles_localA, goles_visA, goles_localB, goles_visB)
print(Ganador_torneo)

""" 
Las denominaciones de las monedas actualmente disponibles en un país son: 20, 
50, 100, 200, 500 y 1000. Escriba una función que reciba la cantidad de monedas 
de cada denominación que tiene una persona y el valor de un producto y le diga 
si es posible pagar el producto con el dinero en efectivo que tiene. Ayuda: 
tiene que revisar si tiene suficiente dinero y, si tiene más de lo necesario, 
si es posible que le den el cambio con las denominaciones de monedas que se 
encuentran en circulación.
""" 
def puede_pagar(monedas_20, monedas_50, monedas100,  monedas200, monedas500, monedas1000, valor_producto):
    dinero_total = monedas_20 * 20 + monedas_50 * 50 + monedas100 * 100 + monedas200 * 200 + monedas500 * 500 + monedas1000 * 1000
    cambio = dinero_total - valor_producto
                
            

""" 
Picas y Fijas es un juego en el que dos personas intentan adivinar un número de
4 dígitos que mantiene en secreto el otro jugador. En cada turno, un jugador 
propone un número de 4 dígitos y el otro jugador debe informar la cantidad de 
picas y la cantidad de fijas de ese número. Cada pica significa que en el número 
propuesto hay un dígito que también está en el número secreto, pero en una 
posición diferente. Cada fija significa que en el número propuesto hay un número 
que también está en el número secreto y que está en la misma posición. 
Por ejemplo, si el número secreto es 5678 y el número que el otro jugador propone
es 6579, la respuesta sería *2 picas y 1 fija” porque 5 y 6 están en las 
posiciones equivocadas y porque el 7 está en la posición correcta. El ganador 
del juego es el jugador que encuentre el número del otro en la menor cantidad de
intentos. En este ejercicio usted debe escribir dos funciones: la primera 
calculará la cantidad de picas dados un número secreto entre 1000 y 9999, y un 
número propuesto también entre 1000 y 9999; la segunda función calculará la 
cantidad de fijas y recibirá también un número secreto y un número propuesto.
""" 

""" 
Un número primo es un número que es divisible sólo por 1 y por sí mismo. 
Los primeros 10 números primos son 2, 3, 5, 7, 11, 13, 17, 19, 23 y 29. 
Escriba una función que dado un número diga cuál es el menor de los primeros 
diez números primos por el que es divisible o retorne -1 si no es divisible por 
ninguno de esos números.
""" 

"""
En una competencia sólo pueden participar estudiantes universitarios que sean 
menores de 23 años o que cumplan 23 años durante el año en curso. Además, pueden 
participar todos los estudiantes universitarios que hayan cursado menos de 2 años 
de estudios en la Universidad. Escriba una función que reciba el año de nacimiento
de una persona y el año de entrada a la universidad y retorne un valor de verdad 
indicando si la persona puede participar o no. 
""" 

"""
En una ciudad existe una restricción de circulación para los vehículos que depende
del número de la placa, del tipo de vehículo, del día de la semana y de la hora 
del día. Los vehículos particulares sólo tienen restricción de lunes a viernes, 
dependiendo del último dígito de su placa: los que terminen en un número par no 
podrán circular entre 6:00 y 8:30 y 15:00 y 19:30 en los días del mes que sean 
pares; los que terminen en un número impar no podrán circular en los mismos 
horarios, pero de los días del mes que sean impares. La restricción para los 
taxis va desde las 5:30 hasta las 21:30, de lunes a sábado: los taxis cuya placa 
termine en el mismo dígito en que termine el día del mes no podrán circular ese 
día. Escriba una función que diga si un vehículo puede circular o no dados: 
el tipo de vehículo (str, TAXI o PARTICULAR), la placa (str, por ejemplo DMZ042), 
el día del mes (int, entre 1 y 31), el día de la semana (str - Lunes, Martes, 
Miércoles, Jueves, Viernes, Sábado o Domingo), la hora (int, entre 0 y 23) y el 
minuto (int, entre 0 y 59).
"""
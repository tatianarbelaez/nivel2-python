# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
1. Escriba una función que reciba una cadena de caracteres y una letra. Su función 
debe retornar la misma cadena que recibió, pero cambiando todas las vocales por 
la letra que también llegó por parámetro. Por ejemplo, si la cadena original era 
“Hola, Mundo!” y la letra entregada fue ‘I’, el resultado debería ser 
“HIlI, MIndI!”.
"""
cadena = 'Tatiana ama a jorge'                #que solicite un string como entrada 
largo=len(cadena)                                    #para obtener el largo asi no cometemos errores
inicio=0                                                     #es una variable necesaria para comparar en un bucle   
cadena_final=""                                                      # Le será de utilidad crear en este problema un string vacío ‘’  
caracter="i"                                               #valor que tomará dependiendo de que letra sea 
while inicio < largo:                                  #inicia el bucle en 0 y lo compara con el largo, se repetirá mientras sea menor   
    if cadena[inicio] in "aeiou":                     #Para acceder a un elemento de un string utilice los corchetes [] donde inicio se irá incrementando
        cadena_final+= cadena.replace(cadena[inicio], caracter)                                # Recuerde que el operador + etc, bien a la cadena vacia le agrego el valor que tiene caracter
        inicio+=1
    else:
        exit()
                                 # si es caracter vale "+"  
                                         #debo incrementar el valor inicial de inicio para que llegue a ser igual que el largo de la caden
print(cadena)                                        #optativo, la cadena original
print(cadena_final)                                             #resultado que finalmente se va a imprimir.(lo pedido, así que es obligatorio)
input()
"""
2. Escriba una función que reciba dos cadenas de caracteres. La función debe retornar 
1 si las cadenas son idénticas, 2 si las cadenas sólo se diferencian por las 
mayúsculas y minúsculas, o 0 de lo contrario.
"""
def cadenas_diferentes(cadena1: str, cadena2: str):
    if cadena1 == cadena2:
        return 1 
    elif cadena1.lower() == cadena2.lower():
        return 2 
    else: 
        return 0 
cadena1 = 'Tatiana'
cadena2 = 'tatianar'
las_cadenas_son_diferentes = cadenas_diferentes(cadena1, cadena2)
print(las_cadenas_son_diferentes)
"""
3. Escriba una función que reciba dos cadenas de caracteres que sólo van a contener 
letras mayúsculas y minúsculas. La función debe retornar -1 si en un diccionario 
la primera cadena debería ir antes que la segunda, debe retornar 1 si la segunda 
cadena debe ir antes que la primera, o 0 si las dos cadenas son la misma 
(ignorando mayúsculas y minúsculas).
"""
def primero_diccionario(cad1: str, cad2: str):
    if cad1 > cad2:
        return 1
    elif cad1 < cad2:
        return -1
    elif cad1 == cad2:
        return 0 
cad1 = 'a'
cad2 = 'c'
cadena_va_primero_en_diccionario = primero_diccionario(cad1, cad2)
print(cadena_va_primero_en_diccionario)
"""
4. Escriba una función que reciba una cadena de caracteres y cuente las palabras que 
aparecen en la cadena. Usted puede suponer que la cadena tendrá letras 
(mayúsculas y minúsculas) y espacios, pero no tendrá ningún signo de puntuación 
ni espacios seguidos.
"""
def contar_palabras(cadena_frase: str):
    numero_espacios = cadena_frase.count(' ')
    numero_palabras = numero_espacios + 1
    return numero_palabras

cadena_frase = 'Martha fue hoy a trabajar'
numero_de_palabras = contar_palabras(cadena_frase)
print(numero_de_palabras)
    
"""
5. Tres equipos de futbol participaron en un pequeño torneo en que jugaron entre 
ellos 3 partidos. Escriba una función que reciba el nombre de los tres equipos 
y los marcadores de los tres partidos, y que retorne una tabla con las posiciones 
de los equipos al finalizar el torneo. La función recibirá entonces 9 parámetros: 
primero los nombres de los tres equipos y luego 6 enteros con los marcadores de 
los 3 partidos. Cada partido ganado entregaba 3 puntos y cada partido empatado 
entregaba 1 punto. La tabla con el resultado del torneo tiene que ser una cadena 
de caracteres con la información organizada en columnas bien alineadas. Las 
columnas deben estar organizadas de la siguiente forma:

posición,

nombre del equipo,

puntos obtenidos,

partidos jugados,

partidos ganados,

partidos empatados,

partidos perdidos,

goles a favor,

goles en contra,

diferencia de goles
"""
"""
6. Escriba una función que, dada la altura de un edificio, retorne una cadena como 
en el siguiente ejemplo: “Un objeto que cae de un edificio de 30 metros tarda 2.47 
segundos en llegar al piso y alcanza una velocidad de 24.25 metros por segundo.” 
Su programa debe usar las funciones de formato de cadenas.

Ayuda: El tiempo que tarda la caída es igual a la raíz cuadrada de dos veces la 
altura sobre la aceleración de la gravedad (9.8 m/s2). La velocidad que alcanza 
el objeto es igual al tiempo de la caída multiplicado por la aceleración de la 
gravedad.
"""
def velocidad_caida_objeto(altura_edificio):
    tiempo = pow((2 * altura_edificio/9.8),0.5)
    velocidad = tiempo * 9.8
    mensaje = plantilla.format(altura_edificio, tiempo, velocidad)
    return mensaje 

altura_edificio = 40        
plantilla = "Un objeto que cae de un edificio de {0} metros tarda {1: 1f} segundos en llegar al piso y alcanza una velocidad de {2: 1f} metros por segundo. "
calcular_velocidad_caida = velocidad_caida_objeto(altura_edificio)
print(calcular_velocidad_caida)

"""
7. Escriba una función que dados el nombre de un país, la cantidad de habitantes 
en millones y el Producto Interno Bruto en millones de USD, retorne una cadena 
como en el siguiente ejemplo: 
    “Colombia……………..=45 millones=    336599 USD Million”. La primera columna debe 
    estar alineada a la izquierda, debe tener 25 caracteres y ocupar los espacios 
    vacíos con .; la segunda columna debe estar centrada, tener 25 caracteres y 
    ocupar los espacios vacíos con *; la tercera columna debe estar alineada a la 
    derecha, tener 10 caracteres más el espacio ocupado por USD Million y debe 
    ocupar los espacios vacíos con espacios.

"""
def cadena_pais_habitantes_pib(nombre_pais: str, cantidad_habitantes: str, pib: int):
    pib_str = str(pib)
    mensaje = nombre_pais.ljust(25, '.') + '=' + cantidad_habitantes.center(25, '*') + pib_str.rjust(10, ' ') + 'USD Million'
    return mensaje 

nombre_pais = 'Nueva Zelanda'
cantidad_habitantes = '38 millones' 
pib = 238
cadena_pais = cadena_pais_habitantes_pib(nombre_pais, cantidad_habitantes, pib)
print(cadena_pais)
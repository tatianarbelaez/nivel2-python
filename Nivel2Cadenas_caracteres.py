# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
*Caracteres de control

\n  Cambio de línea
\t  Tabulación
"""
print("a\tb\tc" + "\n" + "100\t200\t300")

"""
Operadores y funciones

los operadores <, >, <=, >= hacen comparaciones lexicográficas

Los otros operadores relacionales que podemos aplicar a las cadenas de 
caracteres son “==” y “!=”, los cuales comparan las cadenas caracter por caracter.
int y not saber si una cadena esta incluida en otra o no 
len longitud de la cadena 

"""

'AB' < 'BC'

'AB' < 'ab'

'234' < '345'

'!450' < '345'

'ABC' == 'abc'

'ABC' == 'ABC!'

'3' == '1+2'

"Mundo" in "Hola, Mundo!"

"mundo" not in "Hola, Mundo!"

"!" in "Hola, Mundo!"

'?' not in "Hola, Mundo!"

"Hola, Mundo!" in "Hola, Mundo!"

len("Hola, Mundo!")

len("Hola,\nMundo!")

len("")

len(" ")

len("\t")

"""
RECORDARRRRR
Las cadenas de caracteres en Python son inmutables. Todas las operaciones
que se realicen sobre una cadena siempre van a producir una cadena nueva.
"""


"""
METODOS 
str.lower --> devuelve la cadena toda en minusculas 
str.zfill --> le va a agregar ceros a la izquierda a una cadena, hasta lograr
una cadena de la longitud indicada- cadena.metodo(parametros)*

cadena.lower()
cadena.zfill()
cadena.upper()-->toda la cadena en mayusculas
cadena.title()-->todas las iniciales en mayuscula 
cadena.swapcase()-->cambia mayusculas por minisculas y viceversa
cadena.find() -->Busca la primera posición en la que aparezca la cadena buscada. 
Si no la encuentra retorna -1.
cadena.rfind()-->Busca la primera posición en la que aparezca la cadena buscada,
empezando por la derecha. Si no la encuentra retorna -1.
cadena.count()-->Cuenta cuántas veces está la cadena indicada en otra cadena.
Si no la encuentra se produce un error.
cadena.isnumeric()-->Revisa si todos los caracteres de una cadena son números
cadena.replace()-->Remplaza algunos elementos de una cadena con otros elementos
que llegan como parámetro. El reemplazo puede ser la cadena vacía para eliminar los elementos buscados.
cadena.strip()-->Elimina espacios y cambios de línea al final de una cadena de
caracteres. No elimina ningún elemento que no se encuentre al final de la cadena.
cadena.ljust()-->Amplía la cadena hasta el ancho indicado, alinea el contenido a
la izquierda y llena el espacio vacío con espacios.
cadena.rjust()-->Amplía la cadena hasta el ancho indicado, alinea el contenido
a la derecha y llena el espacio vacío con espacios
cadena.center()-->Amplía la cadena hasta el ancho indicado y centra el contenido.

https://docs.python.org/3.6/library/stdtypes.html#string-methods

*Format
Este método es muy poderoso y permite utilizar repetidamente una cadena como 
plantilla para luego remplazar algunos fragmentos por valor particulares.

"""
str.lower('ABcdEg')
'ABcdEg'.lower()

"abc".zfill(10)
str.zfill("abc", 10)

marca = 'Mercedes'
modelo = 'F357'
anho = 2016
cc = 3.8
sec = 5
plantilla = "Un {0} {1} del {2:d} con motor de {3:.1f} litros es capaz de pasar de 0 a 100 kph en {4:.2f} segundos"
mensaje = plantilla.format(marca, modelo, anho, cc, sec)
print(mensaje)

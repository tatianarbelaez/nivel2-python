# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 20:37:21 2021

@author: user
"""
"""
Enunciado: Los cajeros automáticos usualmente tienen restricciones sobre las
claves (numéricas) que pueden usarse para retirar. Usted debe construir una
función que diga si una clave dada (un número entero con 4 dígitos cuyo primer
dígito no es el 0) es permitida de acuerdo alas siguientes reglas:

*El mismo dígito no puede aparecer más de dos veces.

*No puede haber dígitos consecutivos.

*No puede haber números que empiecen por 19, 200 ni 201.

*El número debe tener al menos tres dígitos diferentes.
"""

"""
Enunciado: Usted ha sido encargado de escribir una función que decida si una
contraseña es lo suficientemente segura para un nuevo sistema. Una contraseña
segura debe tener al menos 10 caracteres y cumplir con al menos 3 de las
siguientes restricciones adicionales:

Debe tener al menos una letra mayúscula y una letra minúscula.

Debe tener al menos un dígito.

Debe tener al menos uno de los siguientes caracteres: !"@$ %&/()=?#

No puede empezar ni terminar con un espacio.
"""

"""
Enunciado: Escriba una función que reciba 3 diccionarios que representen las
coordenadas de 3 puntos en el espacio. Cada diccionario tendrá dos llaves, "x"
y "y", que tendrán asociadas los respectivos componentes de cada coordenada.
Su función debe retornar un valor de verdad que indique si los tres puntos se
encuentran sobre la misma recta o no.
"""

"""
Enunciado: El juego de las Picas y Fijas es un juego matemático muy sencillo,
que consiste en adivinar un número de 4 cifras cuyos dígitos son todos
diferentes. Para esto, el jugador que intenta adivinar deberá decir el número
que cree está escondiendo el otro, y este deberá responder el número de picas y
fijas que tiene ahora el jugador.

Una pica es un dígito que se encuentra en el número a adivinar pero no está en
el lugar correcto, y una fija es un dígito correctamente colocado.

Por ejemplo, si el número a adivinar es 1234, y otro jugador dice 1325, tendrá
dos picas y una fija.

Usted debe crear una función que devuelva un diccionario con las llaves "PICAS"
y "FIJAS" que represente el resultado de la jugada si un jugador trata de
adivinar el numero_secreto con el número intento.
"""
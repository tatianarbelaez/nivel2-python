#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 10:09:50 2021

@author: invitado
"""
"""
Leyes fundamentales en algebra boleana

1.Conmutatividad: Tanto la conjunción como la disyunción son conmutativas, 
así que A ∨ B es equivalente a B ∨ A. También es cierto que A ∧ B es equivalente a B ∧ A

2. Asociatividad: Tanto la conjunción como la disyunción son asociativas, así 
que A ∨ (B ∨ C) es equivalente a (A ∨ B) ∨ C. Además, A ∧ (B ∧ C) es equivalente a (A ∧ B) ∧ C 

3. Distribución: en el álgebra Booleana, la conjunción distribuye sobre la 
disyunción y viceversa. Esto quiere decir que:

A ∧ (B ∨ C) ≡ (A ∧ B) ∨ (A ∧ C)

A ∨ (B ∧ C) ≡ (A ∨ B) ∧ (A ∨ C)

4. Identidad de la conjunción: si se hace una conjunción con el valor verdadero, 
el resultado es el mismo. Es decir que A ∧ Verdadero ≡ A.

5. Identidad de la disyunción: si se hace una disyunción con el valor falso, 
el resultado es el mismo. Es decir que A ∨ Falso ≡ A.

6. Dominación de la conjunción: si se hace una conjunción con el valor falso, 
el resultado es falso. Es decir que A ∧ Falso ≡ Falso

7. Dominación de la disyunción: si se hace una disyunción con el valor 
verdadero, el resultado es verdadero. Es decir que A ∨ Verdadero ≡ Verdadero.

*Negación y equivalencia a falso: es lo mismo decir que una proposición tiene 
un valor falso que decir que su negación tiene un valor positivo. Es decir que 
A ≡ Falso es lo mismo que decir ¬ A ≡ Verdadero. Más aún, B ≡ Verdadero es lo mismo
que decir B, así que A ≡ Falso se puede reescribir como ¬ A

Las leyes o teoremas de De Morgan dicen que:

¬ (P ∧ Q) ≡ ¬ P ∨ ¬ Q

¬ (P ∨ Q) ≡ ¬ P ∧ ¬ Q

xor (or exclusivo): es verdadero cuando exactamente un operando es verdadero.

== (equivalencia): es verdadero cuando los operandos tienen el mismo valor.

!= (desigualdad): es verdadero cuando los operandos tienen valores diferentes.

nand: es falso sólo cuando los dos operandos son verdaderos.

nor: es verdadero sólo cuando los dos operandos son falsos.
"""

#tipo de valor bool que solo puede ser True o False 
def f(x: int)->bool:
    print('f:', x)
    return True

def g(x: int)->bool:
    print('g:', x)
    return False

"""
conjuncion  --> and (se evaluan solo los terminos necesarios si el primero es falso
                     declara la sentencia como falsa sin evaluar los demas)
"""
print("Caso 1 - f and f and f :")
print(f(1) and f(2) and f(3))

print("Caso 2 - f and f and g :")
print(f(1) and f(2) and g(3))

print("Caso 3 - f and g and g :")
print(f(1) and g(2) and g(3))

print("Caso 4 - g and g and g :")
print(g(1) and g(2) and g(3))

"""
disyuncion --> or (si el primer operando de una operación que use el operador or 
                   es verdadero, entonces el valor de la operación será verdadero 
                   y no será necesario evaluar los otros términos.)
"""
print("Caso 1 - f or f or f :")
print(f(1) or f(2) or f(3))

print("Caso 2 - f or f or g :")
print(f(1) or f(2) or g(3))

print("Caso 3 - g or f or g :")
print(g(1) or f(2) or g(3))

print("Caso 4 - g or g or g :")
print(g(1) or g(2) or g(3))

"""
negacion --> not (omo se trata de un operador unario se debe anteponer al operando.
                  Es decir que se usa igual que como se usa el signo - para convertir
                  a un número en su negativo )
"""
print("Caso 1:", not f(1) and f(2))
print(not f(1) and f(2))
print("Caso 2:", not g(1) and f(2))
print(not g(1) and f(2))

"""
OPERADORES RELACIONALES 

< Es menor que 

<= Es menor o igual que

> Es mayor que 

>= Es mayor o igual que

== Es igual a 

!= Es diferente de

is Dos objetos son el mismo

is not Dos objetos no son el mismo

"""

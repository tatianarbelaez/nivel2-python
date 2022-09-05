#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:15:23 2021

@author: invitado
"""

"""
1. Escriba una función que dada la edad de una persona indique si puede manejar 
(tiene que tener al menos 16 años)
"""
def persona_puede_manejar(edad: int)-> bool:
    edad_minima = edad >= 16
    return edad_minima

"""
2. Escriba una función que dada la altura en metros y el peso en kilogramos de 
un adulto diga si está dentro de los rangos típicamente considerados saludables.
Para esto debe usar el Índice de Masa Corporal (BMI), que se calcula como peso/altura2.
Un adulto se considera que tiene sobrepeso cuando su BMI es mayor o igual a 25. 
Un adulto se considera que está bajo de peso cuando su BMI es menor a 18.5.
"""
def peso_saludable(altura:float, peso:float)-> bool:
    BMI = peso/(altura**2)
    sobrepeso = BMI >= 25 
    bajo_peso = BMI < 18.5
    return not sobrepeso and not bajo_peso
peso_saludable(1.76, 76) #retorna verdadero
peso_saludable(1.54, 63) #retorna falso
"""
3. Escriba una función que dados dos números diga si el primero es divisible por el segundo.
"""
def primero_divisible_segundo(num1: int, num2: int) -> bool:
    divisible = num1 % num2 == 0
    return divisible
primero_divisible_segundo(10, 2) 
primero_divisible_segundo(133, 5) 
"""
4. Queremos saber si una persona tiene el dinero suficiente para pagar la cuenta
en un restaurante dados los siguientes parámetros: la cantidad de dinero que tiene
la persona, el valor de la cuenta, si la persona va a dejar propina o no. La propina
corresponde al 10% del valor de la cuenta.
"""
def tiene_para_cuenta(cant_dinero: int, valor_cuenta: int, propina: bool)-> bool:
    if propina == True:
        puede_pagar_cuenta = cant_dinero >= valor_cuenta + valor_cuenta*0.1  
    else:
        puede_pagar_cuenta = cant_dinero >= valor_cuenta 
    return puede_pagar_cuenta
tiene_para_cuenta(5000, 4500, False)
tiene_para_cuenta(3500, 3450, True)
tiene_para_cuenta(4600, 4750, False)


  
    


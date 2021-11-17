# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 13:41:55 2021
@author: Oscar P
"""

'''
Ejercicio 1
Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

nombre = input('Dame tu nombre: ')
a = nombre[::-1]
a.title()
print(a)
print(f'la variable es {a}')
'''




'''
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato 
dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
'''
fecha = input('Ingrese la fecha de nacimiento en formato dd/mm/aaaa ')
print(f'El día es: {fecha[:2]} \nMes: {fecha[3:5]} \naño: {fecha[6:]}')




                 
lista_notas = [[1, 4, 3, 4], [4,3,5,6]]
for i in range(len(lista_notas)):
    for j in range(len(lista_notas)):
        print(f'las notas son: {lista_notas[i][2]}')

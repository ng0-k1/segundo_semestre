# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 16:52:27 2021

@author: Oscar P
"""
from cuadrado import Cuadrado 
lado = int(input('Ingrese los lados del cuadrado: '))
colores = input('Ingrese el color: ')
cuadrado_1 = Cuadrado(lado, colores)
cuadrado_1.lado = 15
print(f'El area del cuadrado es: {cuadrado_1.calcular_area()}')

print(cuadrado_1)

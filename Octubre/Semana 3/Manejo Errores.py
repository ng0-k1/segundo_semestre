# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 17:28:08 2021

@author: Oscar P
"""
from errores import *
resultado = None
a = int(input('Digite un numero: '))
b = 1
try:
    b = int(input('Digite un segundo numero: '))
    '''if a !=b:
        raise NumerosdiferentesException('Los numeros son diferentes')
    '''
    resultado = a/b
except ZeroDivisionError as q:
    print(f'error de {q}, {type(q)}')

except ValueError as q:
    print(f'el error es: {q}')

except Exception as q:
    print(q)

print(a+b)
# -*- coding: utf-8 -*-
"""
@author: Oscar P
"""

class Productos:
    contador_productos = 0
    
    def __init__(self, nombre, precio):
        Productos.contador_productos +=1
        self._id_producto = Productos.contador_productos
        self._nombre = nombre
        self._precio = precio
        
    def __str__(self):
        return f'Id producto: {self._id_producto}, nombre: {self._nombre}, precio: {self._precio}'
    
if __name__ == '__main__':
    aux = True
    while aux != False:
        print('Digite 1 para agregar ')
        print('Digite 2 para salir')
        opc = input('Digite la opción: ')
        if opc == "1":
            producto1 = input('Ingrese el nombre del producto: ')
            precio1 = int(input('Ingrese el valor del producto: '))
            producto = Productos(producto1, precio1)
            print(producto._nombre)
            producto2 = Productos(producto1, precio1)  
            print(producto2)
        if opc == "2":
            aux = False
        else:
            print('Digito una opción invalida')


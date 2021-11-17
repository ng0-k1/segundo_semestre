# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 16:32:31 2021

@author: Oscar P
"""
import random
from Productos import Productos

class Orden:
    contador_orden = 0
    
    def __init__(self, productos):
        Orden.contador_orden += 1 
        self._id_orden = Orden.contador_orden
        self._productos = list(productos)
        
    def agregar_productos(self, producto):
        self._productos.append(producto)
        
    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto
    
    def __str__(self):
        producto_str = " "
        for producto in self._productos:
            producto_str += producto.__str__() + '\n'
        return f'Orden: {self._id_orden}, \n Productos: {producto_str}'

if __name__== '__main__':
    producto2 = Productos('Manzanas', random.randint(1500, 1800))
    producto1 = Productos('Arroz', random.randint(2000, 2300))
    producto3 = Productos('Aceite', random.randint(25000, 32000))
    productos = [producto2, producto1]
    orden1 = Orden(productos)
    print(orden1) 
    
    
    
    
        
            
        

        
        

            
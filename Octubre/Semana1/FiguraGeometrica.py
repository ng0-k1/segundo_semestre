# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 16:41:51 2021

@author: Oscar P
"""

class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        
    def __str__(self):
        return f'el alto es: {self.alto} y el ancho es {self.ancho}'
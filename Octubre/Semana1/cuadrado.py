# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 16:46:00 2021

@author: Oscar P
"""

from FiguraGeometrica import FiguraGeometrica as FG
from Color import Color 

class Cuadrado(FG, Color):
    
    def __init__(self, lado, color):
        #super().__init__(ancho, alto)
        FG.__init__(self, lado, lado)
        Color.__init__(self, color)
        
        
    def calcular_area(self):
        return self.ancho * self.alto
        

    def __str__(self):
        return f'{FG.__str__(self)} {Color.__str__(self)}  '
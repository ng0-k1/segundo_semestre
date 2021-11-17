# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 16:09:55 2021

@author: Oscar P
"""

class FiguraGeometrica :
    def __init__(self,ancho, largo):
        if self._validar(ancho):
            self._ancho = ancho
        else:
            self._ancho = 1
            print(f'Valor erroneo nuestro ancho tomara por obligación un valor de: {self._ancho}')
        if self._validar(largo):
            self._largo = largo
        
    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, ancho):
        if self._validar(ancho):
            self._ancho = ancho
        
    @property
    def largo(self):
        return self._largo
    
    @largo.setter
    def largo(self, largo):
        self._largo = largo
        
    def __str__(self):
        return f'Figura Geometrica tiene el siguiente ancho:{self._ancho}, y el siguiente largo: {self._largo}'
       
    def _validar(self, valor):
        return True if 0 <valor< 50 else False
      
class Definiendo:
    pass
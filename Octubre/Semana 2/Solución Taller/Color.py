# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 16:25:46 2021

@author: Oscar P
"""

class Color:
    def __init__(self, color):
        self._color = color 
        
    @property
    def color(self):
        return self._color
    
    @color.setter 
    def color(self, color):
        self._color = color
        
    
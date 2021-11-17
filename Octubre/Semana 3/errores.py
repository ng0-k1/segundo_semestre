# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 17:56:55 2021

@author: Oscar P
"""

class NumerosdiferentesException(Exception):
    
    def __init__(self, mensaje):
        self.message = mensaje
        
class numerosiguales(Exception):
    
    def __init__(self, mensaje):
        self.message = mensaje
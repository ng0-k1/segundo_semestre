# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 17:03:24 2021
"""
#Llamando al archivo (Para este caso Ejercicio_29.py) y llamando a la clase que necesitamos
#NOTA: Si deseamos renombrar la clase que llamamos agregamos un   as   y le ponemos el nombre que deseamos
#Si se desea llamar diferentes clases de un archivo le diremos clase_1, clase_2  
#SI POR EL CONTRARIO DESEAMOS LLAMAR TODAS LAS CLASES AGREGAMOS UN *
from Ejercicio_29 import Persona

persona_1 = Persona('Juana', 'Valentina', 25, 14785)
print(persona_1)

persona_1.mostrar()
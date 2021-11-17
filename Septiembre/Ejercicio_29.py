# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 16:16:54 2021
"""

'''
#Sobrecarga del operador init 
class Persona:
    #El parametro *datos recibe tuplas, las cuales se identifican al imprimir como ()
    #El parametro **frutas recibe diccionarios los cuales se identificaran como {}
    #NOTA LOS PARAMETROS DE *datos y **frutas PUEDEN SER NOMBRADOS A GUSTO DEL USUARIO
    def __init__(self, nombre, apellido, edad, cedula, *datos, **frutas):
        self.nombre = nombre
        self.apellido = apellido 
        self.edad = edad
        self.cedula = cedula 
        self.datos = datos
        self.frutas = frutas
        
    def mostrar(self):
         print(f'Hola {self.nombre} {self.apellido}, tu edad es: {self.edad}, y tu cedula es: {self.cedula}, {self.datos}, {self.frutas}')
        
persona_n = Persona('Juan', 'Perez', '16', '187995', 2,3,4,5,6, m ='manzanas',p= 'peras')
print (persona_n.mostrar())
'''

#Creamos una clase Padre
class Persona:
    def __init__(self, nombre, apellido, edad, cedula, ):
        #variables privados __ 
        #variables privadas opcionalmente _
        self.__nombre = nombre
        self._apellido = apellido 
        self._edad = edad
        self._cedula = cedula 
        
        
    #PARAMETROS DE GET (@property) y SET (nombre_variable.setter)
    #Parametro para retornar el valor que tiene el nombre
    @property
    def nombre(self):
        print('llamando el metodo get')
        return self.__nombre
    #Parametro para modificar el nombre
    
    @nombre.setter
    def nombre(self, nombre):
        print('llamado el metodo set')
        self.__nombre = nombre
        
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido 
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad 
        
    @property
    def cedula(self):
        return self.cedula
    
    @cedula.setter
    def cedula(self, cedula):
        print('Ejecutando desde el setter')
        self._cedula = cedula 
    
    def __str__(self):
        return f'Hola {self.__nombre} {self._apellido}, tu edad es: {self._edad}, y tu cedula es: {self._cedula}'
    
    #Clase para devolver el valor de las variables
    def mostrar(self):
         print(f'Hola {self.__nombre} {self._apellido}, tu edad es: {self._edad}, y tu cedula es: {self._cedula}')
         



#Clase Hija
class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, cedula, sueldo):
        #Super nos devolvera un objeto, en este caso llamamos al metodo __init__ la cual nos devolvera todas las variables que se han agregado en estas
        super().__init__(nombre, apellido, edad, cedula)
        self.sueldo = sueldo
    

empleado = Empleado('Juan', 'Perez Hernandez', 25, 1875681, 2000000)
print(empleado.nombre)

empleado.__nombre = 'Juan Perez'
empleado._cedula = 123412412
print(empleado)
'''
#Condicional para que esta linea se ejecute solo cuando es ejecutada en el mismo archivo (Ej en este caso si ejecutamos el archivo en Ejercicio_29 nos mostrara estos valores
#Pero si llamaramos el archivo Ejercicio_29.py en otro archivo, estas lineas de codigo no se mostrarian)
if __name__ == '__main__':
    
    persona = Persona('Juan', 'Perez', 25, 18547)
    persona.mostrar()
    
    persona.__nombre = 'David'
    persona.nombre = 'David'
    
    
    print(persona.nombre)
    
    persona.mostrar()
#persona._nombre = 'Juan Camilo'
#persona.mostrar()
'''


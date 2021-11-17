class Metodo_dim:
    variable_clase = "Var Clase"
    
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia



objeto1 = Metodo_dim('Hola Variable Instancia')
objeto2 = Metodo_dim('Hola 2 Variable')
print(objeto1.variable_instancia) # 00fx1520
print(objeto1.variable_clase)
print(objeto2.variable_instancia)# 00fx1521
print(objeto2.variable_clase)


class Tipos_Metodos:
    nombre = "Juan"
    edad = 15
    contador = 0 
    contador_ordenes = 0 
    
    def instancia(self, id_orden):
        Tipos_Metodos.contador_ordenes +=1
        id_orden = Tipos_Metodos.contador_ordenes
        self.apellido = "Perez"
        #self.edad = 12
        print(self.nombre)
        print(self.edad)
        print(self.apellido)
        
    @classmethod  
    def metodo_clase(cls):
        cls.edad = 18
        cls.nombre = "Pedro"
        print(cls.edad)
        print(cls.nombre)
        
    @staticmethod  
    def metodo_estatico():
        
        print('Metodo Estatico')
        
producto1 = 'arroz',2000
producto2 = 'cebollas ' 500

productos = list(producto1, producto2)
        
tip = Tipos_Metodos()
tip.instancia()
tip.metodo_clase()
tip.metodo_estatico()
        
from Figura_Geometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
       
    
    def calcular_area(self):
        try:
            return self.largo*self.ancho
        except:
            print('Valor no adquirido')
    
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}, y el color es: {self.color}'


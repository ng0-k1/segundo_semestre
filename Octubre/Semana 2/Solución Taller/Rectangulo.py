from Figura_Geometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, largo, color):
        FiguraGeometrica.__init__(self, ancho, largo)
        Color.__init__(self, color)
        
    def calcular_area(self):
        return self.ancho * self.largo
    
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}, y el color es: {self.color}'
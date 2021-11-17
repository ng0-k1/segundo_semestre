from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(6, 'Verde')
cuadrado = Cuadrado(1, 'azul')
print(f'Calculo del area: {cuadrado1.calcular_area()}')
print(cuadrado1)


rectangulo = Rectangulo(60, 10, 'Naranja')

print(f'calculo del area: {rectangulo.calcular_area()}')
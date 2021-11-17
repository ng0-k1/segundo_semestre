archivo = open('Prueba\\prueba.txt',
               encoding='utf8')
ruta = 'prueba.txt'
#print(archivo.readline())
#print('\n')
print(archivo.read())


for linea in archivo:
    print (linea)
archivo.close()



archivo_2 = open('prueba2.txt', 'a', encoding='utf8')

archivo_2.write('\nEsto es una prueba de una copia')



archivo_2.close()


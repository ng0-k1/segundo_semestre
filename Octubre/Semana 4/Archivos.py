try:
    archivo = open('prueba2.txt', 'r', encoding= 'utf8')
    a = 'error de conexión'
    #b = input('Ingrese el texto: ')
    print(archivo.readline())
# archivo.write(a)
 #   archivo.write(f'\n{b}')
    
except Exception as e:
    print(f'error {e}')
    

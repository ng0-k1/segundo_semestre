from manejos import ManejoArchivos
nomb_archivo = input('¿Como quiere que se llame el archivo?: ')
extension = input('Terminación del archivo: (Por favor iniciar con .) ')
with ManejoArchivos(nomb_archivo+extension) as archivo:
    archivo.write('Valor de prueba')


    
    
pelicula.nombre()
    
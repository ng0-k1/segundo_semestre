class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __enter__(self):
        print('Leyendo el archivo'.center(50, '-'))
        try:
            self.nombre = open(self.nombre, 'a', encoding= 'utf8')
            return self.nombre
        except Exception as e:
            print(f'Error no pude ubicar el archivo {e}')
            
    
    def __exit__(self, tipo_excepción, valor_excepción, traza_error):
        print('cerramos el archivo'. center(50, '*'))
        try:
            if self.nombre:
                self.nombre.close()
        except Exception as e:
            print('Error al cerrar el archivo {e}')
        
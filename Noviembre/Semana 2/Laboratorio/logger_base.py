import logging as log  
log.basicConfig(level= log.INFO, 
                format='%(asctime)s: %(levelname)s [%(filename)s: %(lineno)s] %(message)s',
                datefmt = '%I; %M: %S',
                handlers= [
                    log.FileHandler('logs_errores.log'),
                    log.StreamHandler()
                           ])
if __name__ == '__main__':
    log.debug('Mensaje debug')
    log.info('Mensaje de información')
    log.warning('Mensajes de advertencia')
    log.error('Mensajes de error')
    log.critical('Mensaje tipo critico')
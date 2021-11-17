from CursorPool import CursorDelPool
from logger_base import log
from Usuarios import Usuarios

class UsuariosDAO:
    '''
    CRUD = CREATE  READ UPDATE DELETE 
    '''
    
    _SELECT = 'SELECT * FROM usuarios ORDER BY id_usuario'
    _INSERTAR  = 'INSERT INTO usuarios(username, password) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE usuarios SET username = %s, password = %s WHERE id_usuario = %s'
    _ELIMINAR = 'DELETE FROM usuarios WHERE id_usuario = %s;'
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionando usuarios')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuarios(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios
    
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug('Insertando usuarios')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug('Actualizando usuario')
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Eliminando usuario')
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount
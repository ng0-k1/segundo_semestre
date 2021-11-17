from Usuarios import Usuarios
from UsuariosDao import UsuariosDAO
from CursorPool import CursorDelPool
from logger_base import log

opcion = None
while opcion != 5:
    print('Opciones \n1 Listar Usuarios \n2 Agregar Usuarios \n3 Modificar Usuarios \n4 Eliminar usuarios')
    print('5 Salir')
    opcion = int(input('Ingrese la opción de su preferencia: '))
    
    if opcion == 1:
        usuarios = UsuariosDAO.seleccionar()
        for usuario in usuarios:
            print(usuario)
            
    elif opcion == 2:
        username = input('Ingrese el alias: ')
        password = input('Escribe la contraseña del usuario: ')
        usuarios = Usuarios(username= username, password= password)
        usuario_insertado = UsuariosDAO.insertar(usuarios)
        print(f'Usuario insertado con exito: {usuario_insertado}')
    
    elif opcion == 3:
        username = input('Ingrese el alias a actualizar: ')
        password = input('Ingrese la contraseña: ')
        id_usuario = int(input('Ingrese el id del usuario a actualizar'))
        usuario = Usuarios(id_usuario= id_usuario, username= username, password= password)
        usuario_actualizado = UsuariosDAO.actualizar(usuario)
        print(f'Usuario actualizado: {usuario_actualizado}')
    
    elif opcion == 4:
        id_usuario = input('Inserte el id del usuario a eliminar: ')
        usuario = Usuarios(id_usuario= id_usuario)
        usuario_eliminar = UsuariosDAO.eliminar(usuario)
        print(f'Usuario eliminado: {usuario_eliminar}')
    
    elif opcion == 5:
        print('Hasta luego')
        opcion = 5
    else:
        print('Digito un valor erroneo \n')
import mysql.connector
conexion = mysql.connector.connect(user ='root',
                                   password = 'prob@nd0',
                                   host = '127.0.0.1',
                                   port = 3306,
                                   database = 'Prueba')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM personas WHERE id_persona IN %s'
            entrada = input('Ingrese el ID de la persona a eliminar (separado por comas): ')
            valores = tuple(entrada.split(','))
            print(valores)
            cursor.execute(sentencia, valores)


            registros_eliminados = cursor.rowcount
            print(f'Total elementos eliminados: {registros_eliminados}')
            conexion.commit()
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error al realizar la consulta {e}')

finally:
    conexion.close()
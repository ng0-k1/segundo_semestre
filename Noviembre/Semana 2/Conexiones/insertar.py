import mysql.connector
conexion = mysql.connector.connect(user ='root',
                                   password = 'prob@nd0',
                                   host = '127.0.0.1',
                                   port = 3306,
                                   database = 'Prueba')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO personas(nombre, apellido) values(%s, %s)'
            valores = ('Carlos', 'Perez')
            cursor.execute(sentencia, valores)
            registros_insertados = cursor.rowcount
            print(f'Total elementos insertados: {registros_insertados}')
            conexion.commit()
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error al realizar la consulta {e}')

finally:
    conexion.close()
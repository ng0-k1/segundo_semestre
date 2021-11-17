import mysql.connector
conexion = mysql.connector.connect(user ='root',
                                   password = 'prob@nd0',
                                   host = '127.0.0.1',
                                   port = 3306,
                                   database = 'Prueba')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE personas SET nombre =%s, apellido = %s WHERE id_persona = %s'
            valores = (
                ('Juan', 'Vegaa', 7),
                ('Laura', 'Pereez', 8))
            cursor.executemany(sentencia, valores)
            registros_insertados = cursor.rowcount
            print(f'Total elementos actualizados: {registros_insertados}')
            conexion.commit()
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error al realizar la consulta {e}')

finally:
    conexion.close()
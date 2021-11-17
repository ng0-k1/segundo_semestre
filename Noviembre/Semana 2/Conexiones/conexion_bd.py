# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 16:13:27 2021

@author: Oscar P
"""
import mysql.connector
conexion = mysql.connector.connect(user ='root',
                                   password = 'prob@nd0',
                                   host = '127.0.0.1',
                                   port = 3306,
                                   database = 'Prueba')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM Personas'
            cursor.execute(sentencia)
            regristro = cursor.fetchall()
            for regis in regristro:
                print(regis)
except Exception as e:
    print(f'Ocurrio un error al realizar la consulta {e}')

finally:
    conexion.close()
    
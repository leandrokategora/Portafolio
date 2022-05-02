import pyodbc
import pandas as pd
import sqlalchemy
import pymssql
""" probamos la conexion a Microsoft SQL Server

"""

direccion_servidor = 'WIN-SERVIDOR-BD/DWGRUPOTOTAL'
nombre_bd = 'DW_central'
nombre_usuario = 'Prueba'
password = 'Prueba_1'

try:
    conexion = pymssql.connect(server="WIN-SERVIDOR-BD\DWGRUPOTOTAL", port="1433", user="sa", password="DWpln21", database="DW_central")
#     conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + direccion_servidor + 'DATABASE=' + nombre_bd + ';UID=' + nombre_usuario + ';PWD=' + password)

#     connection = pyodbc.connect(
#     driver="ODBC Driver 17 for SQL Server",
#     server=direccion_servidor,
#     port='1433',
#     database=nombre_bd,
#     uid=nombre_usuario,
#     pwd=password,
# )
    print('conexion exitosa')
    
except Exception as e:
    print('Ocurrio un error al conectar al SQL Server: ', e)


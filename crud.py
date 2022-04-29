import pyodbc
import pandas as pd
import sqlalchemy

""" probamos la conexion a Microsoft SQL Server

"""

direccion_servidor = 'WIN-SERVIDOR-BD/DWGRUPOTOTAL'
nombre_bd = 'DW_central'
nombre_usuario = 'sa'
password = 'DWpln21'

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + direccion_servidor + 'DATABASE=' + nombre_bd + ';UID=' + nombre_usuario + ';PWD=' + password)



except Exception as e:
    print('Ocurrio un error al conectar al SQL Server: ', e)


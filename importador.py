# Importamos las librerias necesarias (sqlalchemy establece la conexion, pyodbc provee el driver, 
# urllib es para crear la url de conexion y pandas es para manejar la info)
# 
from ast import Break
from logging import exception
import sqlalchemy as sa
import pandas as pd
import pyodbc
import urllib


# Variable desde donde lee el archivo local a cargar
dir_pandas = 'C:/Users/Usuario/portafolio/{}'

# Codigo SQL que se va aejecutar
query = """SELECT * FROM dFuerzadeVentasPruebas;"""

# Parametros con los que se va a crear la URL de conxion a la base
params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};"
                                    "SERVER=WIN-SERVIDOR-BD\DWGRUPOTOTAL;"
                                    "DATABASE=DW_Central;"
                                    "UID=sa;"
                                    "PWD=DWpln21")

# print(parametros_conect + "\n")



def run():
    try:
        engine = sa.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
        print("Conexion Exitosa" + "\n")    

    except Exception:
        print("Error al conectar a la bases de datos" + "\n")
        
    
    df = pd.read_excel(dir_pandas.format('AUXILIARES 2019.XLSX'), sheet_name = 'AUX VENDEDORES')
    print("Datos Leidos: " + '\n')
    print(df.head())

    try:
        df.to_sql('dFuerzadeVentasPruebas', con = engine, if_exists = 'append', index= False)
        df1 = pd.read_sql_query(query, engine)
        print("Carga correcta de los datos" + '\n')
        print(df1.tail(10))
        print("Tamaño del archivo: ")
        print( df1.shape)

    except Exception:
        print("Error al cargar los datos en la base de datos")
        


if __name__=='__main__':
    run()


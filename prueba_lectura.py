# import pandas as pd
# import openpyxl

# dir_pandas = 'C:/Users/Usuario/portafolio/{}'

# df = pd.read_excel(dir_pandas.format('AUXILIARES 2019.xlsx'), sheet_name='AUX VENDEDORES')

# for i in df:
#     print(i)

from sqlalchemy import create_engine
# import pymysql
import pandas as pd
# import pymssql
import pyodbc
import openpyxl
import pymssql



# direccion_servidor = 'WIN-SERVIDOR-BD/DWGRUPOTOTAL'
# nombre_bd = 'DW_central'
# nombre_usuario = 'sa'
# password = 'DWpln21'




dir_datos = "C:/Users/Usuario/portafolio/{}"

# engine = create_engine("mssql+pyodbc://sa:DWpln21@WIN-SERVIDOR-BD/DWGRUPOTOTAL:1433/DW_central")

# engine = create_engine("mssql+pyodbc://sa:DWpln21@WIN-SERVIDOR-BD\DWGRUPOTOTAL:1433/DW_central?driver=ODBC+Driver+17+for+SQL+Server")
# engine = create_engine("DRIVER={ODBC Driver17 for SQL Server}; SERVER = 'WIN-SERVIDOR-BD\DWGRUPOTOTAL'; DATABASE='DW_central';")
# conect = pymssql.connect(server="WIN-SERVIDOR-BD\DWGRUPOTOTAL", port="1433", user="sa", password="DWpln21", database="DW_central")

try:
    engine = create_engine("mssql+pyodbc://Prueba:Prueba_1@WIN-SERVIDOR-BD\DWGRUPOTOTAL:1433/DW_central?driver=ODBC+Driver+17+for+SQL+Server")
    print("conexion enxitosa")

    conect = pyodbc.connect(engine)


    df = pd.read_excel(dir_datos.format('AUXILIARES 2019.xlsx'), sheet_name='AUX VENDEDORES')
    # df1 = pd.read_sql("SELECT Fecha, Codigo, Area FROM Accidentes;", con = engine)
    print('Lectura correcta')

    df.to_sql('dFuerzadeVentasPruebas', con = conect, if_exists = 'append', index= False)
    print("Carga correcta")


except Exception:
    print("\nERROR: Unable to connect to the server.")
    exit(-1)

# except Exception as e:
#     print("Ocurrió un error", e)
# finally:
#     engine.close()
# print('no se pudo leer el archivo de datos')

# df.to_sql('dFuerzadeVentasPruebas', con = engine, if_exists = 'append', index= False)

# print('Carga finalizada')



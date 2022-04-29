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




direccion_servidor = 'WIN-SERVIDOR-BD/DWGRUPOTOTAL'
nombre_bd = 'DW_central'
nombre_usuario = 'sa'
password = 'DWpln21'




dir_datos = 'C:/Users/Usuario/portafolio/{}'

# engine = create_engine("mssql+pyodbc://sa:DWpln21@WIN-SERVIDOR-BD/DWGRUPOTOTAL:1433/DW_central")

engine = create_engine("mssql+pyodbc://sa:DWpln21@WIN-SERVIDOR-BD/DWGRUPOTOTAL:1433/DW_central?driver=ODBC+Driver+17+for+SQL+Server")
df = pd.read_excel(dir_datos.format('AUXILIARES 2019.xlsx'), sheet_name='AUX VENDEDORES')
print('Lectura correcta')


# print('no se pudo leer el archivo de datos')

df.to_sql('dFuerzadeVentasPruebas', con = engine, if_exists = 'append', index= False)

print('Carga finalizada')



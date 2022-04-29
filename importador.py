# from matplotlib.pyplot import table
from sqlalchemy import create_engine
import pymysql
import pandas as pd
import openpyxl
dir_pandas = 'C:/Users/Usuario/portafolio/{}'


db = 'pruebatr'
table1 = 'dFuerzadeVentas'
# path = '\\serverarchivos\archivosGT\PLANEAMIENTO\02-VENTAS\14-Base de Ventas Grupo Total\2016\01-Bases\AUXILIARES 2019.xlsx'

url = "mysql://scott:usuario2'@'localhost/pruebatr"

engine = create_engine('mysql+pymysql://scott:tiger@localhost/pruebatr')
df = pd.read_excel(dir_pandas.format('AUXILIARES 2019.xlsx'), sheet_name='AUX VENDEDORES')


print("read_ok")


df.to_sql(name = table1, con = engine, if_exists= 'append', index = False)


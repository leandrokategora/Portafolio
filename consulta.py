# from crud import conexion21



# try:
#     with conexion21.cursor() as cursor:
#         # En este caso no necesitamos limpiar ningún dato
#         cursor.execute("SELECT Fecha, Codigo, Area FROM Accidentes;")

#         # Con fetchall traemos todas las filas
#         Accidentes = cursor.fetchall()

#         # Recorrer e imprimir
#         for accidente in Accidentes:
#             print(accidente)
# except Exception as e:
#     print("Ocurrió un error al consultar: ", e)
# finally:
#     conexion21.close()
import sqlalchemy as sql
# from sqlalchemy.orm import sessionmaker
import pandas as pd
# import pymssql
import pyodbc
import openpyxl
import pymssql



dir_datos = "C:/Users/Usuario/portafolio/{}"

q_sql = """SELECT * FROM Accidentes"""

engine21 = sql.create_engine('mssql+pyodbc://sa:DWpln21@WIN-SERVIDOR-BD\DWGRUPOTOTAL:1433/DW_central?driver=ODBC+Driver+17+for+SQL+Server')
    
print("conexion enxitosa")
        

# df = pd.read_excel(dir_datos.format('AUXILIARES 2019.xlsx'), sheet_name='AUX VENDEDORES')
# print('Lectura correcta del archivo local')
# for line in df:
#     print(line)


df1 = pd.read_sql_query('''SELECT * FROM DArticulosBebidas''', engine21)
print('Lectura correcta del servidor')
for x in df1:
    print(x)
    # df1.head()

    # df.to_sql('dFuerzadeVentasPruebas', con = conect, if_exists = 'append', index= False)
print("Carga correcta")
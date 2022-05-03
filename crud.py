# winpty python
#  python -i

from matplotlib.pyplot import connect
import pyodbc
import pandas as pd
import sqlalchemy
import pymssql
""" probamos la conexion a Microsoft SQL Server

"""

dir_datos = "C:/Users/Usuario/portafolio/{}"
direccion_servidor = 'WIN-SERVIDOR-BD/DWGRUPOTOTAL'
nombre_bd = 'DW_central'
nombre_usuario = 'Prueba'
password = 'Prueba_1'
table1 = "fuerzaVentasPrueba"

try:
    conexion21 = connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};UID=sa;PWD=DWpln21;SERVER=WIN-SERVIDOR-BD\DWGRUPOTOTAL;DATABASE=DW_central;')
    # conexion21 = pymssql.connect(server="WIN-SERVIDOR-BD\DWGRUPOTOTAL", port="1433", user="sa", password="DWpln21", database="DW_central")
#     conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + direccion_servidor + 'DATABASE=' + nombre_bd + ';UID=' + nombre_usuario + ';PWD=' + password)
    print('conexion exitosa')

    query = """SELECT * FROM Accidente;"""

    df_2 = pd.read_sql_query(query, conexion21)
    print(df_2.head(5))
    for x in df_2:
        print(x)
        print("\n")




    df = pd.read_excel(dir_datos.format('AUXILIARES 2019.xlsx'), sheet_name='AUX VENDEDORES')
    print(df.head(5))
    for i in df:
        print(i)
        print("\n")

    df.to_sql(name = table1, con = conexion21, if_exists = 'append', index = False)
    print("Carga correcta")
#     connection = pyodbc.connect(
#     driver="ODBC Driver 17 for SQL Server",
#     server=direccion_servidor,
#     port='1433',
#     database=nombre_bd,
#     uid=nombre_usuario,
#     pwd=password,
# )
    

except Exception as e:
    print('Ocurrio un error al conectar al SQL Server: ', e)


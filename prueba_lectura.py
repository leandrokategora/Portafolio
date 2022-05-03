# """ importamos dependencias!"""


# import pandas as pd
# import openpyxl

# dir_pandas = 'C:/Users/Usuario/portafolio/{}'

# df = pd.read_excel(dir_pandas.format('AUXILIARES 2019.xlsx'), sheet_name='AUX VENDEDORES')

# for i in df:
#     print(i)

# from requests import Session, session
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import pymysql
import sqlalchemy as sa
# from sqlalchemy.orm import sessionmaker
import pandas as pd
# import pymssql
import pyodbc
import openpyxl
import urllib
# import pymssql



# direccion_servidor = 'WIN-SERVIDOR-BD/DWGRUPOTOTAL'
# nombre_bd = 'DW_central'
# nombre_usuario = 'sa'
# password = 'DWpln21'


# "declaramos variables"

dir_datos = "C:/Users/Usuario/portafolio/{}"

q_sql = """SELECT * FROM Accidentes"""

# engine = create_engine("mssql+pyodbc://sa:DWpln21@WIN-SERVIDOR-BD/DWGRUPOTOTAL:1433/DW_central")

# engine = create_engine("mssql+pyodbc://sa:DWpln21@WIN-SERVIDOR-BD\DWGRUPOTOTAL:1433/DW_central?driver=ODBC+Driver+17+for+SQL+Server")
# engine = create_engine("DRIVER={ODBC Driver17 for SQL Server}; SERVER = 'WIN-SERVIDOR-BD\DWGRUPOTOTAL'; DATABASE='DW_central';")
# conect = pymssql.connect(server="WIN-SERVIDOR-BD\DWGRUPOTOTAL", port="1433", user="sa", password="DWpln21", database="DW_central")

# "intentamos crear la conexion y"

try:
    #engine = sql.create_engine("mssql+pyodbc://sa:DWpln21@WIN-SERVIDOR-BD/DWGRUPOTOTAL:1433/DW_central")
    # engine12 = sa.create_engine("""mssql+pyodbc://sa:DWpln21@WIN-SERVIDOR-BD\DWGRUPOTOTAL/
    #                             DW_Central?driver={ODBC Driver17 for SQL Server}""")
    
    #engine21 = sql.create_engine('mssql+pyodbc://sa:DWpln21@WIN-SERVIDOR-BD/DWGRUPOTOTAL:1433/DW_central?driver=ODBC+Driver+17+for+SQL+Server')
    # engine21 = sql.create_engine("mssql+pyodbc://DRIVER={ODBC Driver 17 for SQL Server};SERVER=WIN-SERVIDOR-BD/DWGRUPOTOTAL:1433;DATABASE=DW_central;UID=sa;PWD=DWpln21");

    # conn_str = (
    # r'Driver=ODBC Driver 17 for SQL Server;'
    # r'Server=WIN-SERVIDOR-BD/DWGRUPOTOTAL;'
    # r'Database=DW_central;'
    # r'Trusted_Connection=Yes;')

    params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};"
                                    "SERVER=WIN-SERVIDOR-BD\DWGRUPOTOTAL;"
                                    "DATABASE=DW_Central;"
                                    "UID=sa;"
                                    "PWD=DWpln21")
    print(params + "\n")

    engine12 = sa.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))


    # quoted_conn_str = urllib.parse.quote_plus(conn_str)
    # engine = create_engine("mssql+pyodbc://sa:DWpln21@SERVIDOR-BD/DWGRUPOTOTAL:1433/DW_central,")


    print("conexion enxitosa","\n")

        

    df = pd.read_excel(dir_datos.format('AUXILIARES 2019.xlsx'), sheet_name='AUX VENDEDORES')
    # for i in df:
    #     print(i)
    print(df.head())

    
    # for line in df:
    #    print(line)

    query = """SELECT * FROM Accidente;"""

    print('Lectura correcta del archivo local',"\n")

    df_2 = pd.read_sql_query(query, engine12)
    print(df_2.head())
    # for x in df_2:
    #     print(x)

    # df1 = pd.read_sql_query('''SELECT * FROM ArticulosBebidas''', engine)
    # print('Lectura correcta del servidor',"\n")
    # for x in df1:
    #     print(x)
    # # df1.head()

    # df.to_sql('dFuerzadeVentasPruebas', con = engine12, if_exists = 'append', index= False)
    print("Carga correcta")


except Exception:
    print("\nERROR: sigue intentando infeliz!")
    exit(-1)

# except Exception as e:
#     print("Ocurrió un error", e)
# finally:
#     engine.close()
# print('no se pudo leer el archivo de datos')

# df.to_sql('dFuerzadeVentasPruebas', con = engine, if_exists = 'append', index= False)

# print('Carga finalizada')



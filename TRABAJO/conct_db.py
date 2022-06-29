from logging import exception
import sqlalchemy as sa
import urllib


parameters = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};"
                                     "Server=WIN-SERVIDOR-BD\DWGRUPOTOTAL;"
                                     "DATABASE=DW_Central;"
                                     "UID=sa;"
                                     "PWD=DWpln21")


try:
    enginex = sa.create_engine("mssql+pyodbc:///?odbc_connect={}".format(parameters))
    print("Conect succesfull")
except Exception:
    print("Errora in DataBase conection")

    


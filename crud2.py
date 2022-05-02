# import pyodbc 
# cnxn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=WIN-SERVIDOR-BD/DWGRUPOTOTAL:1433;DATABASE=DW_central;UID=Prueba;PWD=Prueba_1");


# cursor = cnxn.cursor()
# cursor.execute('SELECT Fecha, Codigo, Area FROM Accidentes;')

# for row in cursor:
#     print('row = %r' % (row,))


import pymssql

try:
    conn = pymssql.connect(server="WIN-SERVIDOR-BD\DWGRUPOTOTAL", port="1433", user="sa", password="DWpln21", database="DW_central")
    # cursor = conn.cursor()
    # cursor.execute ("SELECT Fecha, Codigo, Area FROM Accidentes;")
    # row = cursor.fetchone()
    # print(f"\n\nSERVER VERSION:\n\n{row[0]}")
    # cursor.close()
    # conn.close()
except Exception:
    print("\nERROR: Unable to connect to the server.")
    exit(-1)
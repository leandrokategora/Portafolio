import pandas as pd

# import cdata as cmod 
# conn = cmod.connect("User=Prueba@WIN-SERVIDOR-BD\DWGRUPOTOTAL;Password=Prueba_1;")


# cur = conn.cursor()
# cur.execute("SELECT * FROM DAccidentes")
# rs = cur.fetchall()
# for row in rs:
#     print(row)

dir_datos = "C:/Users/Usuario/portafolio/{}"
df = pd.read_excel(dir_datos.format('AUXILIARES 2019.xlsx'), sheet_name='AUX VENDEDORES')
for i in df:
    print(i)
    
import cdata as cmod 
conn = cmod.connect("User=Prueba@WIN-SERVIDOR-BD\DWGRUPOTOTAL;Password=Prueba_1;")


cur = conn.cursor()
cur.execute("SELECT * FROM DAccidentes")
rs = cur.fetchall()
for row in rs:
    print(row)


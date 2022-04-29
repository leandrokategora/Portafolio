from crud import conexion



try:
    with conexion.cursor() as cursor:
        # En este caso no necesitamos limpiar ningún dato
        cursor.execute("SELECT Fecha, Codigo, Area FROM Accidentes;")

        # Con fetchall traemos todas las filas
        Accidentes = cursor.fetchall()

        # Recorrer e imprimir
        for accidente in Accidentes:
            print(accidente)
except Exception as e:
    print("Ocurrió un error al consultar: ", e)
finally:
    conexion.close()
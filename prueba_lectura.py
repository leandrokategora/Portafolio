import pandas as pd
import openpyxl

dir_pandas = 'C:/Users/Usuario/portafolio/{}'

df = pd.read_excel(dir_pandas.format('AUXILIARES 2019.xlsx'), sheet_name='AUX VENDEDORES')

for i in df:
    print(i)


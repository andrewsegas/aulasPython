import pandas as pd
from pandas import ExcelWriter
import openpyxl
  
df = pd.read_excel("arquivos/excelExemplo.xlsx")

'''print("imprimir o range do index")
print(df.index)

print("imprimir os cabecalhos")
print(df.columns)

print("imprimir 'Livro' e as informacoes das colunas:")
print(df['Livro'])
'''

# imprime cada linha da coluna
for i in df.index:
    print(df['Livro'][i])

# write the dataframe back out with the new column data included
writer = ExcelWriter('Pandas-Example-Out.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()
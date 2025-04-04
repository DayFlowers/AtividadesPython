import pandas as pd
# print(pd.__version__)
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print(df.head())


df.set_index("PassengerId",inplace=True) #consultas atraves do index

print(df.head(12))
#comandos
"""print(df.columns) # saber o nome de uma coluna
df.values()
df.describe ()
print(df.loc[1]) # numero do elemento ex:1° dado 
print(df.loc[[1,2,3]])#pode localizar varios de uma vez fazendo uma lista
print(df.loc[[1,2],['Name','Sex','Age']])
print(df.loc[10:20])#slice
print(df.loc[10:30:2])de qual a qual de dois em dois"""
print(df.loc[1:10,['Name','Sex','Age']])
print(df.query('Age>20').head())
print(df.query('Age>20'))
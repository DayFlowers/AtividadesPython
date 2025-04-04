#grafico com salarios minimos de 2000 á 2025 com os valores dos salarios

import matplotlib.pyplot as plt 

ano=(2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025)
salario=(151, 180, 200, 240, 260, 300, 350, 380, 415, 465, 510, 545, 622, 678, 724, 788, 880, 937, 954, 998, 1045, 1100, 1212, 1302, 1320,1340)

bars=plt.bar(ano,salario,color='green')


plt.ylabel(u'Salário') #u(utf) tem que colocar pra não dar erro nas palavras
plt.xlabel(u'Ano')
plt.title("Salário Minimo dos Anos")


plt.xticks(ano,rotation=62)#legenda um por um 
plt.bar_label(bars,labels=[f'{v:.2f}'for v in salario],padding=4)


plt.grid(True) #pra colocar uma grade

plt.show()
import matplotlib.pyplot as plt 

a=(10,20,30) #só uma variavel

explode=(0.1,0,0)# sai o pedaço do grafico
labels=["HB20","Gol","Fusca"]
plt.pie(a,explode=explode,labels=labels,autopct='%.2f%%', shadow=True)
plt.title('Meu Grafico')
plt.grid(True)

plt.show()
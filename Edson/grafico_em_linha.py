import matplotlib.pyplot as plt #Como fazer graficos 

a=(1,2,3,4,5)
b=(1,2,3,4,5,)

plt.plot(a,b)


#legendas 
plt.ylabel(u'Alguns numeros y') #u(utf) tem que colocar pra não dar erro nas palavras
plt.xlabel(u'Alguns numeros x')
plt.title("El Graficulo")



plt.show() #sempre colocar por último


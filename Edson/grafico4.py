import matplotlib.pyplot as plt #Como fazer graficos 


plt.plot ((1,2,3,4),(1,4,9,16), 'mD:') #concatenando a e b na mesma linha. 'mD:' é comando de:m- de cor magenta D- de quadrado :- linha pontilhada 

plt.axis((0,6,0,20)) #axis é pra aumentar a escala 0 onde inicia 6 onde finaliza apenas para dar uma maximizada no grafico

plt.grid(True) #pra colocar uma grade

plt.show() #sempre colocar por último


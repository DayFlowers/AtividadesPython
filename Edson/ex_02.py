#candidatos a prefeitura

"""import matplotlib.pyplot as plt 

votos=(36,45,19) #só uma variavel

explode=(0.1,0,0)# sai o pedaço do grafico
labels=["Maria","João","Miguel"]
plt.pie(votos,explode=explode,labels=labels,autopct='%.2f%%', shadow=True)
plt.title('Meu Grafico')
plt.grid(True)

plt.show()"""

import matplotlib.pyplot as plt

# Values of candidates
candidato1 = 40
candidato2 = 35
candidato3 = 25

# Candidate names
candidatos = ['Candidato 1', 'Candidato 2', 'Candidato 3']

# Voting values
valores = [candidato1, candidato2, candidato3]

# Creating the bar chart
plt.bar(candidatos, valores, color=['blue', 'green', 'red'])

# Adding title and labels
plt.title('Distribuição de Votos dos Candidatos')
plt.xlabel('Candidatos')
plt.ylabel('Percentual de Votos')

# Display the chart
plt.ylim(0, 100)
plt.show()

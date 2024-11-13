#30.	Histograma de Ocorrências em Lista: Crie uma função histograma(lista) que recebe uma lista e retorna um dicionário com o número de ocorrências de cada elemento da lista. 
def histograma(lista):
    ocorrencias = {}
    for item in lista:
        if item in ocorrencias:
            ocorrencias[item] += 1  # Incrementa o contador se o item já estiver no dicionário
        else:
            ocorrencias[item] = 1  # Adiciona o item ao dicionário com contador 1
    return ocorrências
lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
resultado = histograma(lista)
print(resultado)  # Saída: {1: 1, 2: 2, 3: 3, 4: 4}

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, nome, quantidade):
        if nome in self.produtos:
            self.produtos[nome] += quantidade
        else:
            self.produtos[nome] = quantidade
        print(f'{quantidade} unidades de {nome} adicionadas ao estoque.')

    def remover_produto(self, nome, quantidade):
        if nome in self.produtos and self.produtos[nome] >= quantidade:
            self.produtos[nome] -= quantidade
            print(f'{quantidade} unidades de {nome} removidas do estoque.')
        else:
            print(f'Não há estoque suficiente de {nome}.')

    def verificar_estoque(self, nome):
        return self.produtos.get(nome, 0)

# Exemplo de uso
estoque = Estoque()
estoque.adicionar_produto("Pão de hambúrguer", 100)
estoque.remover_produto("Pão de hambúrguer", 20)

# Verificar estoque
print("Estoque de Pão de hambúrguer:", estoque.verificar_estoque("Pão de hambúrguer"))

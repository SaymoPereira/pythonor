class CarrinhoDeCompra:
    def __init__(self):
        self.produtos = []

    def inserirProduto(self, produto):
        self.produtos.append(produto)  # Ligando as duas classes

    def listaProduto(self):
        c = 1
        for produto in self.produtos:
            print(f'{c} - {produto.nome}: {produto.valor}')  # Trazendo informações da classe produto
            c += 1

    def somaTotal(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

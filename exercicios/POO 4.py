class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        pass

    #GETTER
    @property
    def get_preco(self):
        return self._preco

    #SETTER
    @property
    def preco(self, value):
        self._preco = value


p1 = Produto('Camisa', 50)
p1.desconto(10)
print(p1.preco)

p2 = Produto('Caneca', 20)
p2.desconto(15)
print(p2.preco)

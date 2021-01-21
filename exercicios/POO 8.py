from classPOO8 import *

carrinho = CarrinhoDeCompra()

p1 = Produto('Camisa', 70)
p2 = Produto('PS5', 4899)
p3 = Produto('Short', 30)

carrinho.inserirProduto(p1)
carrinho.inserirProduto(p2)
carrinho.inserirProduto(p3)

carrinho.listaProduto()
print(carrinho.somaTotal())

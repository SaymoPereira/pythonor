from clas import *

escritor = Escritor('João')
print(escritor.nome)

caneta = Caneta('BIC')
print(caneta.marca)

maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta  # Associação entre objetos -> Atributo de escritor recebendo um inteiro
escritor.ferramenta.escrever()
escritor.ferramenta.marca()

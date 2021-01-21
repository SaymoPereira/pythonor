class cliente():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = []

    def insereEndereco(self, cidade, estado):
        self.endereco.append(enderecos(cidade, estado))  # Ligando as duas classes

    def listaEndereco(self):
        for enderecos in self.endereco:
            print(f'{enderecos.cidade} - {enderecos.estado}')  # Listando informações da classe endereco

    def __del__(self):
        print(f'{self.nome} foi apagado')


class enderecos:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade} - {self.estado} foi apagado')

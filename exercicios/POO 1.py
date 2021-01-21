class meuObj(object):  # Criando classes
    #def __init__(self):  # Construtor OU
    def __init__(self, n, i):
        self.nome = n
        self.idade = 0
        print('Construtor chamado com sucesso!')

    def imprime(self):
        print(f'Olá meu nome é {self.nome} tenho idade {self.idade} anos')


pessoa = meuObj('Saymo', 17)
pessoa.imprime()

pessoa.nome = 'And'
print(pessoa.nome)

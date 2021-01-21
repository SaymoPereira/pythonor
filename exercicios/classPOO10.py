class Cliente:
    def __init__(self, cpf, nome, sobrenome):
        self.cpf = cpf
        self.nome = nome
        self.sobrenome = sobrenome


class historico:  # Essa classe só é criada após o instanciamento de um objeto da classe conta -> Composição
    def __init__(self):
        self.transacoes = []

    def imprime(self):
        print('-'*40)
        print('Transações: ')
        for i in self.transacoes:
            print(f'- {i}')


class Conta:
    def __init__(self, numero, agencia, cliente, saldo=0):
        self.numero = numero
        self.agencia = agencia
        self.titular = cliente
        self.saldo = saldo
        self.historico = historico()  # Composição -> A classe histórico está sendo criada dentro da classes cliente

    def depositar(self, value):
        self.saldo += value
        self.historico.transacoes.append(f'Valor {value} depositado!')  # Acessando o atributo histórico que contém
        # um objeto no qual existe um atributo chamado transações

    def sacar(self, value):
        if self.saldo < value:
            print('Saldo menor que o valor de saque!')
            return
        self.saldo -= value
        self.historico.transacoes.append(f'Valor {value} sacado!')

    def statusConta(self):
        print('-'*40)
        print(f'Nome - {self.titular.nome} {self.titular.sobrenome}\n'  # Pegando informações do objeto Cliente
              f'Número - {self.numero}\n'
              f'Agência - {self.agencia}\n'
              f'Saldo - {self.saldo}')

    def transferir(self, conta_destino, value):
        self.saldo -= value
        conta_destino.saldo += value
        self.historico.transacoes.append(f'Foi transferido: {value}')

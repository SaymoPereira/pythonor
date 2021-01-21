from datetime import date


class Pessoa:  # Criando um 'objeto'
    anoAt = date.today().year  # Var global da classe pessoa

    def __init__(self, nome, idade, comendo=False, falando=False):  # Método construtor
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

        '''var = 'valor'  # Var de escopo, só funciona dentro desse método e dentro dessa classe
        print(var)'''

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} está comendo não pode falar!')
            return

        if self.falando:
            print(f'{self.nome} já está falando!')
            return

        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def pararFalar(self):
        if not self.falando:
            print(f'{self.nome} não está falando!')
            return
        self.falando = False
        print(f'{self.nome} parou de falar!')

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo!')
            return
        if self.falando:
            print(f'{self.nome} está falando, não pode comer!')
            return

        print(f'{self.nome} está comendo {alimento}!')
        self.comendo = True

    def pararComer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo nada!')
            return

        print(f'{self.nome} parou de comer!')
        self.comendo = False

    def MostraPessoa(self):
        print(f'Olá sou {self.nome} tenho idade de {self.idade}')

    def get_ano_nascimento(self):
        return self.anoAt - self.idade


p1 = Pessoa('Saymo', 17)  # Criando um objeto
'''# p1.MostraPessoa()
# print(p1.comendo)
# p1.comer('Carne')
# p1.pararComer()
# p1.pararComer()
p1.comer('maça')
# print(p1.comendo)
p1.falar('anime')
p1.pararComer()
p1.falar('anime')
p1.falar('anime')
p1.pararFalar()
p1.comer('pão')
p1.pararComer()
p1.falar('batata')'''

print(p1.anoAt)
print(Pessoa.anoAt)
print(p1.get_ano_nascimento())

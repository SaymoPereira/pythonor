class Npc:
    def __init__(self, nome, time, forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100

    def status(self):
        print(f'Nome: {self.nome}\n'
              f'Time: {self.time}\n'
              f'Força: {self.forca}\n'
              f'Munição: {self.municao}\n'
              f'Estado: {"Vivo" if self.vivo else "Morto"}\n'
              f'Energia: {self.energia}')
        print('-'*42)


class Soldado(Npc):
    def __init__(self, nome, time):  # Esse contrutor sobrescreve o construtor da classe pai
        self.forca = 200
        self.municao = 200
        super().__init__(nome, time, self.forca, self.municao)  # Invocando o construtor da classe pai e passando parâm.


class Guarda(Npc):
    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 20
        super().__init__(nome, time, self.forca, self.municao)


class Elite(Npc):
    def __init__(self, nome, time):
        self.forca = 400
        self.municao = 500
        super().__init__(nome, time, self.forca, self.municao)
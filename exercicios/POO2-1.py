from datetime import date


class Pessoa:
    anoAt = date.today().year

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.anoAt - self.idade)

    @classmethod    # cls se refere a classe
    def por_ano_nascimento(cls, nome, ano_nascimento):  # Método de classe
        idade = cls.anoAt - ano_nascimento
        return cls(nome, idade)


# p1 = Pessoa('Pereira', 25)
p1 = Pessoa.por_ano_nascimento('Luiz', 1987)  # Criando um objeto pelo Método de classe
print(p1.idade)
p1.get_ano_nascimento()

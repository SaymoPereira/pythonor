'''
    public, private, protected -> Outras linguagens

    $Python -> RESPEITAR A CONVENÇÃO

    _  -> 'PRIVADO' - Mas de uma maneira fraca, ainda pode ser alterado.
    __ -> 'Fortemente PRIVADO' - (_NOMECLASSE__NOMEATRIBUTO)
'''


class BaseDados:
    def __init__(self):
        self.__dados = {}  # -> FORTEMENTE PRIVADO

    @property
    def get_dados(self):
        return self.__dados

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})  # Funde/atualiza dicionários

    def listar_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(f'{id} - {nome}')

    def apagar_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDados()

bd.inserir_clientes(1, 'Marie')
bd.inserir_clientes(2, 'James')
bd.inserir_clientes(3, 'Curie')

bd.__dados = 'batata'
# print(bd.__dados)  # -- > Ao fazer isso o python cria uma var com mesmo nome e instância da super protegida e é
# possivel acessa- lá normalmente

# bd.listar_clientes()

print(bd.get_dados)
# print(bd._BaseDados__dados)

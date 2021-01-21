from classPOO10 import *

c1 = Cliente(1454110, 'João', 'Silva')
conta1 = Conta('0303030', '1524-7', c1, 200)  # Associando um cliente a uma conta

conta1.sacar(150)
conta1.statusConta()

conta1.depositar(1050)
conta1.statusConta()

conta1.historico.imprime()

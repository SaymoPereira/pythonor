from lib.arquivo import *
from lib.interface import *
from time import sleep

arq = 'usuarios.txt'
rel = 'relatorio.txt'

if not arquivoExiste(arq):
    criaArquivo(arq)
if not arquivoExiste(rel):
    cabecalho(rel)

while True:
    escolha = menu(['Listar Usuários', 'Cadastrar Usúario', 'Ver Relatório', 'Sair do Sistema'])

    if escolha == 1:
        lerUsuario(arq)
    elif escolha == 2:
        nome = input('Digite o seu nome:').strip().capitalize()
        espaco = leiaFloat('Digite o espaço ocupado:[Kilobytes]')
        cadastrar(arq, nome, espaco)
    elif escolha == 3:
        relatorio(arq)
    elif escolha == 4:
        sleep(0.5)
        cabecalho('Saindo do Sistema...Até logo!')
        break
    else:
        print('\033[31mERRO:\033[31m A opção escolhida é INVÁLIDA!')
    sleep(2)

from ex115.lib.interface import *  # Importando tudo
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):  # Verifica se o arquivo não existe, se não existir, cria
    criarArquivo(arq)

while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoa', 'Sair do Sistema'])  # Recebe o retorno da def leiaInt

    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('Novo Cadastro')
        nome = input('Digite seu nome:').strip()
        idade = leiaInt('Digite sua idade:')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('\033[35mSaindo do Sistema... Volte sempre!\033[m')
        break
    else:
        print('\033[31mErro: Opção inválida, digite novamente!\033[m')
    sleep(2)


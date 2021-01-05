from ex115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')  # Tenta abrir o arquivo para leitura(r) em modo txt(t)
        a.close()  # Fecha o arquivo
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')  # Escreve um arquivo(w) de texto(t) se ele não existir, crie(+)
        a.close()
    except:
        print('\033[31mHouve um erro na criação do arquivo!\033[m')
    else:
        print(f'\033[32mArquivo \033[36m{nome}\033[m \033[32mcriado com sucesso!\033[m')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo!\033[m')
    else:
        cabecalho('Pessoas Cadastradas')
        for c in a:
            dado = c.split(';')
            dado[1] = dado[1].replace('\n', '')  # Removendo a quebra de linha colocada na hr do cadastro
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

        #  print(a.read())  # ou readlines -> Lê o arquivo
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')  # Colocando coisas no arquivo(a -> append no arquivo) de texto(t)
    except:
        print('\033[31mHouve um erro na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')  # Escreve dentro do arquivo
        except:
            print('\033[31mHouve um erro na hora de escrever os dados!\033[m')
        else:
            print(f'\033[32m{nome} cadastrado com sucesso!\033[m')  # Usúario cadastrado com sucesso!
            a.close()

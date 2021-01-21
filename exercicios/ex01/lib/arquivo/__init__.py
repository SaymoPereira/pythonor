from ex01.lib.interface import *


def criaArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mERRO\033[31m: Falha ao criar arquivo!')
    else:
        print('Arquivo criado com sucesso!')


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def lerUsuario(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mERRO:\033[31m Falha ao ler o arquivo!')
    else:
        cabecalho('Usúarios Cadastrados')
        c = 1
        for lin in a:
            dado = lin.split(';')
            dado[1] = dado[1].replace('\n', '')
            if c == 1:
                print(f'{"Nome":<30}{"Espaço"}')
            print(f'{dado[0]:<30}{dado[1]:>3}')
            c += 1
    finally:
        a.close()


def cadastrar(arq, nome, esp):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mERRO\033[31m: O arquivo não pode ser aberto para cadastro!')
    else:
        try:
            a.write(f'{nome};{esp/1024}\n')
        except:
            print('\033[31mERRO:\033[31m Não foi possivel cadastrar!')
        else:
            print(f'\033[32mUsuário {nome} cadastrado com sucesso!\033[m')


def relatorio(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('\033[31mERRO:\033[m O arquivo não pode ser aberto!')
    else:
        try:
            c = 1
            for lin in a:
                dado = lin.split(';')
                dado[1] = dado[1].replace('\n', '')
                if c == 1:
                    print(f'{"N°":<3}{"Nome":<10}{"Dados":>3}')
                print(f'{c:<3}{dado[0]:<10}{dado[1]:>3} MB')
                c += 1
        except:
            print('\033[31mERRO:\033[m Não consegui ler os arquivos!')
        finally:
            a.close()

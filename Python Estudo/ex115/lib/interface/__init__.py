def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('Erro! Digite um número INTEIRO válido!')
            continue
        except KeyboardInterrupt:
            return 0
        else:
            return n


def linha(tam=42):
    print('-' * tam)


def cabecalho(txt):
    linha()
    print(txt.center(42))
    linha()


def menu(lst):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lst:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    linha()
    op = leiaInt('\033[32mSua opção:\033[m')  # Lê a opção escolhida pelo usuário
    return op  # Retorna o que o usuário escreveu
    linha()

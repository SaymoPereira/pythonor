def linha():
    print('-'*42)


def leiaInt(n):
    while True:
        try:
            num = int(input(n))
        except (TypeError, ValueError):
            print('\033[31mERRO:\033[m Digite um número INTEIRO válido!')
            continue
        except KeyboardInterrupt:
            return 0
        else:
            return num


def leiaFloat(n):
    while True:
        try:
            num = float(input(n))
        except (ValueError, TypeError):
            print('Escreva um número REAL válido!')
        except KeyboardInterrupt:
            return 0
        else:
            return num


def cabecalho(msg):
    linha()
    print(msg.center(42))
    linha()


def menu(lst):
    cabecalho('Menu Principal')
    c = 1
    for item in lst:
        print(f'{c} - {item}')
        c += 1
    linha()
    op = leiaInt('Sua opção:')
    return op
    linha()

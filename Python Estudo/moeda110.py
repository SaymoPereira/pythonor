def diminuir(num=0, taxa=0, formato=False):
    res = num - (num * taxa / 100)
    return res if not formato else moeda(res)


def aumetar(num=0, taxa=0, formato=False):
    res = num + (num * taxa / 100)
    return res if not formato else moeda(res)


def dobro(num=0, formato=False):
    res = num * 2
    return res if not formato else moeda(res)


def metade(p=0, formato=False):
    res = p / 2
    return res if not formato else moeda(res)


def moeda(preco=0, moeda='R$'):
    res = f'{moeda}{preco:>.2f}'.replace('.', ',')
    return res


def resumo(preco=0, taxa=10, red=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'preço analisado: \t{moeda(preco)}')  # Tabulação, deixar bonitim
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Com {taxa}% de aumento:\t{aumetar(preco, taxa, True)}')
    print(f'Com {red}% de desconto:\t{diminuir(preco, red, True)}')
    print('-' * 30)

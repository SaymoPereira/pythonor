def diminuir(num=0, taxa=0):
    res = num - (num * taxa / 100)
    return res


def aumetar(num=0, taxa=0):
    res = num + (num * taxa / 100)
    return res


def dobro(num=0):
    res = num * 2
    return res


def metade(p=0):
    return p / 2


def moeda(preco=0, moeda='R$'):
    res = f'{moeda}{preco:>.2f}'.replace('.', ',')
    return res

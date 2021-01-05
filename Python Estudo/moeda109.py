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

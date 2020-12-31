from time import sleep


def linha():
    print('-=' * 30)


def contar(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    if i < f:
        linha()
        print(f'Contando de {i} até {f} pulando de {p} em {p}')
        for d in range(i, f + 1, p):
            print(d, end=' ')
            sleep(0.3)
        print()
        linha()
    else:
        linha()
        cont = i
        print(f'Contando de {f} até o {i} pulando de {p} em {p}')
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont -= p
        print()
        linha()


contar(1, 10, 1)
contar(10, 1, 2)

print('Escolha!')
ini = int(input('Inicio:'))
fim = int(input('Fim:'))
pas = int(input('Passo:'))

contar(ini, fim, pas)

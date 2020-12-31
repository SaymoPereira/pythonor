from random import randint


def sorteia(lista):
    for cont in range(0, 5):
        lista.append(randint(1, 10))

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
        print(f'{valor}', end=' ')
    print(f'Somando os valores pares temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
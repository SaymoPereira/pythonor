'''def soma(a, b):  # Definindo funções com paramêtros
    s = a + b
    print(s)'''


def soma(*num):
    s = 0
    for c in num:
        s += c
    print(f'Somando os valores {num} temos {s}')


soma(5, 2)
soma(4, 8, 6)


def contador(*num):  # Empacotando paramêtros, não sei quantos são, mas os que vierem joga ai em num
    print(f'Você passou {len(num)} números foram eles {num}')


'''
contador(1, 25, 4, 8, 10, 11, 12)
contador(1, 25, 4, 8, 10, 11, 12, 1, 25, 4, 8, 10, 11, 12, 1, 25, 4, 8, 10, 11, 12)
contador(1, 25)
soma(7, 7)
'''


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 5, 4, 8, 9]
dobra(valores)
print(valores)

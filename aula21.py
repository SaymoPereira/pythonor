'''  help(print()) ou print(input.__doc__)

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    """
    cont = i
    while cont <= f:
        print(f'{cont}', end=' ')
        cont += p
    print('END!')


contador(1, 100, 10)
help(contador)'''

'''def somar(a=0, b=0, c=0):
    """
    -> Faz a soma e mostra o resultado na tela
    :param a:1 valor
    :param b:2 valor
    :param c:3 valor
    """
    s = a+b+c
    print(f'A soma dos números é {s}')


somar(4, 5, 10)
somar(4, 3)
somar(5)'''

'''
def teste(b):
    global a  # faz com que não cria outra VAR, mas sim utilize a global
    a = 8  # O programa fica com duas variaveis A -> Uma Local(função) e outra Global(programa)
    b += 4
    print(f'A dentro vale {a}\n'
          f'B dentro vale {b}')


a = 5
print(f'A fora vale {a}')
teste(a)'''

'''
def somar(a=0, b=0, c=0):
    s = a+b+c
    return s


r1 = somar(5,  2)
r2 = somar(5, 5, 7)
r3 = somar(1, 1, 2)
print(r1, r2, r3)'''


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(4)
f2 = fatorial(7)
f3 = fatorial(6)
print(f1, f2, f3)
n = int(input('Digite um número:'))
print(f'O fatorial de {n} é {fatorial(n)}')

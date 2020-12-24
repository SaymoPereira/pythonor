from random import randint
u = 0
n = randint(1, 10)
palpite = 0
print('-=' * 12)
print('Oi pensando em um número entre 0 e 10, tente adivinha-ló')
print('-=' * 12)

while n != u:
    n = randint(1, 10)
    u = int(input('Digite um valor:'))
    print(f'Valor pensado {n} seu valor {u}')
    palpite += 1
    if u == n:
       print(f'Parabéns! Você acertou depois de {palpite} palpites')

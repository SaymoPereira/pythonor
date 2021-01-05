from random import randint

pal = int(input('Quandos palpites deseja?'))
n = []
jogos = []
tot = 1
while tot <= pal:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in n:
            n.append(num)
            cont += 1
        if cont >= 6:
            break
    n.sort()
    jogos.append(n[:])
    n.clear()
    tot += 1
print('-='*3, f'Sorteando {pal} jogos', '-='*3)
for c, n in enumerate(jogos):
    print(f'Jogo {c+1} : {n}')

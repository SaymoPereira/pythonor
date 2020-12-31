from random import randint
from time import sleep
from operator import itemgetter

j1 = randint(1, 6)
j2 = randint(1, 6)
j3 = randint(1, 6)
j4 = randint(1, 6)

jogo = {
    'Jogador 1': j1,
    'Jogador 2': j2,
    'Jogador 3': j3,
    'Jogador 4': j4
}

ranking = dict()

print('-='*30, '\n'
    f'{"Jogando Dados":^60}')
print('-='*30)

#  Apresentando lista de jogadores
for k, v in jogo.items():
    print(f' {k} jogou {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)  # Colocando o dicionário em ordem

print('-'*40)
print(f'    == Ranking dos Jogadores ==')
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)

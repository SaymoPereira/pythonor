from random import randint
j1 = randint(1, 6)
j2 = randint(1, 6)
j3 = randint(1, 6)
j4 = randint(1, 6)

jogo = {
    'jogador 1': j1,
    'jogador 2': j2,
    'jogador 3': j3,
    'jogador 4': j4
}
print('-='*30, '\n'
    f'{"Jogando Dados":^60}')
print('-='*30)

#  Apresentando lista de jogadores
for k, v in jogo.items():
    print(f'Jogador {k} jogou {v}')
print('-'*50)

maior = 0
jm = ''

for e in enumerate(jogo):
    for k, a in jogo.items():
        if e == 0:
            maior = a
            jm = k
        else:
            if maior < a:
                maior =a
                jm = k
print(f'O maior número foi {maior} e o vencedor é {jm}')

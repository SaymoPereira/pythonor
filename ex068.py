from random import randint

jogador = tot = v = 0


while True:
    jogador = int(input('Digite um número:'))
    pc = randint(0, 10)
    tot = pc + jogador
    escolha = ' '
    while escolha not in 'pi':
        escolha = input('Par ou Impar? [P/I]').strip().lower()[0]
    print(f'Você jogou {jogador} e eu {pc} com total de {tot}', end='')
    print('Deu PAR' if tot % 2 == 0 else 'Deu IMPAR')
    if escolha == 'p':
        if tot % 2 == 0:
            print('YOU VICTORY')
            v += 1
        else:
            print('YOU LOSER')
            break
    elif escolha == 'i':
        if tot % 2 == 1:
            print('YOU VICTORY')
            v += 1
        else:
            print('YOU LOSER')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você ganhou {v} vezes')
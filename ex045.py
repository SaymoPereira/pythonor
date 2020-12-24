from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
acao = randint(0, 2)

print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura
''')

user = int(input('Qual sua jogada?'))

print('-=' * 12)
print('O jogador escolheu {}'.format(itens[user]))
print('O PC escolheu {}'.format(itens[acao]))
print('-=' * 12)

if user == acao:
    print('EMPATE!')
elif user == 0 and acao == 1 or user == 1 and acao == 2 or user == 2 and acao == 0:
   print('Você PERDEU!')

elif user == 0 and acao == 2 or user == 1 and acao == 0 or user == 2 and acao == 1:
    print('Você GANHOU!')
else:
    print('Opção INVÁLIDA!')
print('-='*12, '\n', '10 termos de uma PA', '\n', '-='*12)
p = int(input('Qual o primeiro termo da PA?'))
r = int(input('Qual a razão?'))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} =>', end=' ')
        termo += r
        cont += 1
    print('Pausa mané')
    mais = int(input('Quantos termos você quer ver a mais?'))
print(f'A PA foi finalizada com {total} termos mostrados!')
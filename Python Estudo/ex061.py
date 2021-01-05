print('-='*12, '\n', '10 termos de uma PA', '\n', '-='*12)
p = int(input('Qual o primeiro termo da PA?'))
r = int(input('Qual a razão?'))
termo = p
cont = 1
while cont <= 10:
    print(f'{termo} =>', end=' ')
    termo += r
    cont += 1
print('Fim mané')
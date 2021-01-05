print('-='*12, '\n', '10 termos de uma PA', '\n', '-='*12)
p = int(input('Qual o primeiro termo da PA?'))
r = int(input('Qual a razão?'))
decimo = p + (10 - 1) * r

for c in range(p, decimo + r, r):
    print('{}'.format(c), end=' => ')
print('Fim')

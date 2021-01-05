print('-='*12, '\nSequência de Fibonassi\n', '-='*12)

n = int(input('Quantos termos você quer mostrar?'))
t1 = 0
t2 = 1
print('-'*30)
print('{} => {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'{t3}')
    t1 = t2
    t2 = t3
    cont += 1

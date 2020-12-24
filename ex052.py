n = int(input('Digite para sabermos se o número é primo:'))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print(f'\n\033[32mO número {n} foi divisivel {cont} vezes\033[m')

if cont == 2:
    print('\033[35mO número é primo!')
else:
    print('\033[35mEle não é primo!')

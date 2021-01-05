lista = []
cont = 0

while True:
    lista.append(int(input('Digite um número:')))
    cont += 1
    op = ' '
    while op not in 'sn':
        op = input('Quer continuar? [S/N]').strip().lower()[0]
    if op == 'n':
        break
print(f'Você digitou {cont} números')
print(f'Você digitou os números {lista.sorted(reverse = True)}')
if 5 in lista:
    print('Número 5° foi digitado')
else:
    print('Número 5° não foi digitado')


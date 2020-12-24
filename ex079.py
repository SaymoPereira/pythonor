lista = list()
while True:
    n = int(input('Digite um número:'))
    if n not in lista:
        lista.append(n)
        print('Valor cadastrado!')
    else:
        print('Valor já cadastrado!')
    op = ' '

    while op not in 'sn':
        op = input('Deseja continuar? [S/N]').strip().lower()[0]
    if op == 'n':
        break
lista.sort()
print(f'Você digitou os valores {lista}')

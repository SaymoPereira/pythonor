lista = listap = listai = []

while True:
    lista.append(int(input('Digite um número:')))

    op = ' '
    while op not in 'sn':
        op = input('Quer continuar? [S/N]').strip().lower()[0]
    if op == 'n':
        break

for c in lista:
    if c % 2 == 0:
        listap = [c]
    else:
        listai = [c]
print(f'Você digitou os números {lista}\n'
      f'{listap} são pares\n'
      f'{listai} são impares')
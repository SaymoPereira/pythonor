from datetime import date
at = date.today().year

menor = 0
maior = 0

for c in range(1, 8):
    nasc = int(input(f'Digite sua data de nascimento da {c} pessoa:'))
    idade = at - nasc
    print('Ela tem {}'.format(idade))
    if idade <= 21:
        menor += 1
    else:
        maior += 1
print(f'Ao total foram {maior} maiores de idade e {menor} menores de idade!')

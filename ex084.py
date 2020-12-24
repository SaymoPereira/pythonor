princ = list()
temp = []

while True:
    temp.append(input('Digite seu nome:'))
    temp.append(float(input('Digite seu peso:')))
    if len(princ) == 0:
        mai = men = 0
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()

    resp = input('Quer continuar? [S/N]').strip().lower()[0]
    if resp in 'n':
        break
print('*'*30)
print(f'Os dados foram {princ} \n'
      f'Ao total {len(princ)} cadastradas')

print(f'O maior peso foi {mai}Kg. Peso de ', end='')
for p in princ:
    if princ[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi {men}Kg. Peso de ', end='')
for p in princ:
    if princ[1] == men:
        print(f'[{p[0]}]', end='')

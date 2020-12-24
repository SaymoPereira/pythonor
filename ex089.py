aluno = list()
op = ' '

while True:
    nome = input('Nome:').strip()
    n1 = float(input('Nota 1:'))
    n2 = float(input('nota 2:'))
    media = (n1 + n2) / 2

    aluno.append([nome, [n1, n2], media])

    op = input('Deseja continuar? [S/N]').lower()
    if op == 'n':
        break

print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)

for i, a in enumerate(aluno):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')

while True:
    print('-'*35)
    opc = int(input('Informar notas de qual aluno? [999 para parar]'))

    if op == 999:
        break
    if op <= len(aluno) - 1:
        print(f'Notas de {aluno[opc][0]}  são {aluno[opc][1]}')
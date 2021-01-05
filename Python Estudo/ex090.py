n = input('Nome:').strip()
n1 = int(input('Nota 1:'))
n2 = int(input('Nota 2:'))
media = (n1 + n2) / 2
situacao = ''

if media > 6:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'

aluno = {
    'nome': n,
    'nota 1': n1,
    'nota 2': n1,
    'média': media,
    'situacao': situacao
}
escola = list()
escola.append(aluno.copy())

print('-='*30)
for a in escola:
    for k, v in a.items():
        print(f'  - {k} é igual a {v}')

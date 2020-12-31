galera = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome:')

    while True:
        pessoa['sexo'] = input('Sexo[M/F]:').upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor insira um código válido!')

    pessoa['idade'] = int(input('Idade:'))
    soma += pessoa['idade']

    galera.append(pessoa.copy())

    while True:
        op = input('Quer continuar? [S/N]').lower().strip()[0]
        if op in 'sn':
            break
        print('Erro! Por favor insira um código válido!')

    if op == 'n':
        break

print('-='*30)
print(f'A) Temos {len(galera)} pessoas cadastradas!')
media = soma / len(galera)
print(f'B) A média das idades é {media:5.2f}')
print(f'C) As mulheres cadastradas foram', end=' ')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()

print('D) Lista das pessoas que estão acima da média' , end=' ')
for p in galera:
    if p['idade'] > media:
        print(' ', end='')
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')

print()
print('< Encerrado >')

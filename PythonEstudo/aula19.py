'''pessoa = {
    'nome': 'Saymo',
    'sexo': 'M',
    'idade': 17
}

print(f'O {pessoa["nome"]} do sexo {pessoa["sexo"]} tem idade de {pessoa["idade"]} anos')
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

pessoa['nome'] = 'José'
pessoa['peso'] = 54.4

# del pessoa['sexo']

for k, v in pessoa.items():
    print(f'{k} = {v}')'''

'''brasil = []
estado1 = {'uf': 'Ceará', 'sigla': 'Ce'}
estado2 = {'uf': 'Pará', 'sigla': 'Pa'}

brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])'''

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa:')
    estado['sigla'] = input('Sigla:')
    brasil.append(estado.copy())  # Cria uma cópia, age do mesmo modo que [:] em uma lista
# print(brasil)

for e in brasil:  # Para a lista
    for k, v in e.items():  # Para o dicionário
        print(f'{k} = {v}')

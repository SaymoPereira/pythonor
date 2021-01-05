import moeda

p = float(input('Digite um número:'))

print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'{moeda.moeda(p)} aumentado em 10% é {moeda.moeda(moeda.aumetar(p, 10))}')
print(f'O dobro de {moeda.moeda(p)} vale {moeda.moeda(moeda.dobro(p))}')
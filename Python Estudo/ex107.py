import moeda

p = float(input('Digite um número:'))

print(f'A metade de {p:.2f} é {moeda.metade(p):.2f}')
print(f'{p:.2f} aumentado em 10% é {moeda.aumetar(p, 10):.2f}')
print(f'O dobro de {p:.2f} vale {moeda.dobro(p)}')

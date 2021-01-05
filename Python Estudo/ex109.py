import moeda109

p = float(input('Digite um número:'))

print(f'A metade de {moeda109.moeda(p)} é {moeda109.metade(p, True)}')
print(f'{moeda109.moeda(p)} aumentado em 10% é {moeda109.aumetar(p, 10, True)}')
print(f'O dobro de {moeda109.moeda(p)} vale {moeda109.dobro(p, True)}')
print(f'Diminuindo em 12% e {moeda109.diminuir(p, 12, True)}')

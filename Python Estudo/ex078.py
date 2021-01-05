lista = posicaomaior = posicaomenor = []
for pos, c in enumerate(range(0, 5)):
    lista.append(int(input(f'Digite um número para o posição {pos}:')))

print(f'Você digitou os números {lista}')
print(f'O maior valor é {max(lista)} e está nas posições {lista.index(max(lista))}\n')
print(f' o menor é {min(lista)} e está nas posições {lista.index(min(lista))}')

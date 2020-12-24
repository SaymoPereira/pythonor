lista = []

for c in enumerate(range(1, 6)):
    n = int(input('Digite um número:'))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')
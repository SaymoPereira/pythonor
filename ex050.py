s = 0
cont = 0
for c in range(1, 7):
    c = int(input(f'Digite {c} valor:'))
    if c % 2 == 0:
        s += c
        cont += 1
print(f'A soma de todos os números {cont} pares é de: {s}')

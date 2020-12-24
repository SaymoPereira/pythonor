matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# alimentando a matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um número para [{linha}, {coluna}]:'))
print('-='*30)

# Exibindo a matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

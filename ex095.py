time = list()
partidas = list()
jogador = dict()

while True:
    jogador.clear()
    jogador['nome'] = input('Nome:').strip()
    part = int(input('Quantas partidas?'))
    partidas.clear()

    for c in range(1, part+1):
        partidas.append(int(input(f'    Quantos gols na partida {c}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)  # Soma valores

    time.append(jogador.copy())

    while True:
        resp = input('Quer continuar? [S/N]').strip().lower()[0]
        if resp in 'sn':
            break
        print('Informações inválidas! Preencha novamente!')
    if resp == 'n':
        break
print('-='*30)

for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para sair]'))

    if busca == 999:
        break

    if busca > len(time):
        print(f'Erro! não existe jogador com o código inserido!')
    else:
        print(f'--- Levantamento do jogador {time[busca]["nome"]}---')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g}')
    print('-'*40)
print('< VOLTE SEMPRE >')
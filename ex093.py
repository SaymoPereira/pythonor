nome = input('Nome:').strip()
part = int(input('Quantas partidas?'))
s = 0
listag = []
for c in range(1, part+1):
    gol = int(input(f'Quantos gols na partida {c}?'))
    listag.append(gol)
    s += gol


def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {g} gols')

n = input('Nome do jogador:').strip(),
g = input('Total de gols:').strip()

if g.isnumeric():  # Verifica se o número pode ser númerico
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gol=g)
else:
    ficha(n, g)
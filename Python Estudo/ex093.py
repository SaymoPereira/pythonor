nome = input('Nome:').strip()
part = int(input('Quantas partidas?'))
s = 0
listag = []
for c in range(1, part+1):
    gol = int(input(f'Quantos gols na partida {c}?'))
    listag.append(gol)
    s += gol

jogador = {
    'nome': nome,
    'partidas': part,
    'gols': listag[:],
    'total': s
}

print('-='*30)
print(jogador)
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')

for c, n in enumerate(listag):
    print(f'    => Na partida {c+1}, fez {n} gols')
print(f'Com total de {jogador["total"]} de gols')
print('-=' * 30)

for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')

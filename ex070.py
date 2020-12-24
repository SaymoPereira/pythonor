s = preco = contp = cont = 0
nome = resp = menor = nomem = ''

while True:
    print('-'*20)
    nome = input('Digite o nome do produto:')
    preco = float(input('Digite seu preço:'))
    resp = input('Quer continuar? [S/N]').strip().lower()[0]
    s += preco
    cont += 1
    while resp not in 's n':
        resp = input('Informação INVÁLIDA! Deseja continuar?')
    if resp == 'n':
        break
    if preco > 1000:
        contp += 1
    if cont == 1:
        menor = preco
        nomem = nome
    else:
        if preco < menor:
            menor = preco
            nomem = nome
print(f'O total gasto foi de {s:.2f}\n'
      f'{contp} produto com mais de R$ 1000,00\n'
      f'O produto mais barato foi {nomem}')

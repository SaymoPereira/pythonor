from datetime import date
atual = date.today().year
dados = dict()

dados['nome'] = input('Nome:').strip()
nasc = int(input('Ano de Nascimento:'))
dados['idade'] = atual - nasc
dados['ctps'] = int(input('Carteira de trabalho [0 se não tiver]:'))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação:'))
    dados['salário'] = float(input('Salário:'))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - atual
print('-='*30)
for k, v in dados.items():
    print(f'    - {k} tem valor {v}')
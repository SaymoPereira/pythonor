casa = float(input('Digite o valor da casa:'))
salario = float(input('Digite salário do Comprador:'))
ano = int(input('Digite em quantos anos deseja pagar:'))

prest = casa / (ano * 12)

if prest > salario - (salario * 70/100):
    print('A prestação é {:.2f} sua compra foi Negada, pois prestações ultrapassam 30% da sua renda'.format(prest))
else:
    print('Para comprar a casa no valor de {} sua prestação mensal é {:.2f}'.format(casa, prest))

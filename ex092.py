from datetime import date
atual = date.today().year

nome = input('Nome:').strip()
nasc = int(input('Ano de Nascimento:'))
idade = atual - nasc
tb = int(input('Carteira de trabalho [0 não tem]:'))
if tb > 1:
    contrato = int(input('Ano de contratação:'))
    salario = float(input('Salário:'))

pessoa = {
    'nome': nome,
    'idade': idade,
    'CTPS': tb,
    'contrato': contrato,
    'salário': salario
}
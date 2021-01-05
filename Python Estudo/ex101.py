from datetime import date


def voto(nasc):
    atual = date.today().year
    idade = atual - nasc
    if idade < 16:
        print(f'Com idade: {idade} anos: Não pode votar!')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com idade {idade} anos: o voto é opcional!')
    else:
        print(f'Com idade {idade} anos: Voto é obrigatório!')


voto(int(input('Informe sua idade de nascimento:')))
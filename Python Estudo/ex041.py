from datetime import date

at = date.today().year
nas = int(input('Digite sua data de nascimento:'))

idade = at - nas

if idade <= 9:
    print('Categoria Mirim!')
elif idade <= 14:
    print('Categoria Infantil!')
elif idade <= 19:
    print('Categoria Junior!')
elif idade <= 20:
    print('Categoria Sênior!')
else:
    print('Categoria Master!')

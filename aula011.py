'''
Cores no terminal

\033['style','text','back' m => para colocar as cores

ex:

033[0;33;44m
styles: 1 => negrito, 4 => underline, 7 => inverter as cofigurações
text: 30 ao 37 => cada número é uma cor diferente
back: 40 ao 47 => cada número é uma cor diferente
'''

print('\033[1;31;43mOlá, mundo!\033[m')
print('\033[1;33;45mOlá, mundo!\033[m')

a = 5
b = 8

print(f'Os valores são \033[32m{a}\033[m e \033[33m{b}\033[m')

cores = {
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'pretoebranco':'\033[32m'

}
nome = 'Saymo'

print('Olá, prazer conhece-ló {}{}'.format(cores['azul'],nome))

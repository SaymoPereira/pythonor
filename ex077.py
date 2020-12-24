palavras = ('Aprender', 'Programar', 'Python', 'Linguagem', 'Curso')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
print('\n', '-'*40)
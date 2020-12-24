maior = 0
nomev = ''
mulher = 0
s = 0

for c in range(1, 5):
    print(f'---- {c}ª PESSOA ----')
    n = input('Nome:').strip()
    idade = int(input('Idade:'))
    sexo = input('Sexo [M/F]:').strip().lower()

    s += idade
    if c == 1 and sexo == 'm':
        maior = idade
        nomev = n
    if sexo == 'm' and idade > s:
            maior = idade
            nomev = n
    if sexo == 'f' and idade < 20:
        mulher += 1

print('A idade média do grupo foi {:.2f} o mais velho é {} tem idade de {} ao todo são mulher(es) {} com menos de 20 anos'.format(s/4, nomev, maior, mulher))
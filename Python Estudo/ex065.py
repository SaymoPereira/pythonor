maior = menor = cont = s = 0
t = 's'

while t in 'Ss':
    n = int(input('Digite um número inteiro:'))
    cont += 1
    s += n
    t = input('Deseja continuar? [S/N]').strip().upper()[0]

    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

media = s / cont
print('Você digitou {} números a média entre eles é {:.2f} o menor número foi {} e o maior {}'.format(cont, media, menor, maior))

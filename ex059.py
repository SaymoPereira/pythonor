from time import sleep

n1 = float(input('Digite o 1° valor:'))
n2 = float(input('Digite o 2° valor:'))
op = 0
maior = 0

while op != 5:
    print('=-'*12)
    op = int(input('\033[34m[MENU]\033[m\n'
        '[1] Somar\n'
        '[2] Multiplicar\n'
        '[3] Maior\n'
        '[4] Novos Números\n'
        '[5] Sair do Programa\n'
        'Escolha uma opção:'))
    print('=-' * 12)
    if op == 1:
        s = n1 + n2
        print('A soma entre os números {} e {} é {}'.format(n1, n2, s))
    elif op == 2:
        s = n1 * n2
        print('A multiplicação entre os números {} e {} é {}'.format(n1, n2, s))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif op == 4:
        n1 = float(input('Digite novamente o 1° valor:'))
        n2 = float(input('Digite novamente o 2° valor:'))
    else:
        print('Opção inválida!!!')
        break
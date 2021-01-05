def leiaint(num):
    ok = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'Escreva um número válido!')
        if ok:
            break
    return valor


n = leiaint('Digite um número:')
print(f'Você digitou o valor {n}')
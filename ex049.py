p = int(input('Suas opções:\n'
              '[0] Soma\n'
              '[1] Subtração\n'
              '[2] Multiplicação\n'
              'Digite qual operação quer efetuar:'))
t = int(input('Digite um número para sabermos a tabuada:'))

if p == 0:
    for c in range(10, -1, -1):
        s = c + t
        print('{} + {} = {}'.format(t, c, s))
elif p == 1:
    for c in range(-1, 10):
        s = (c - t) * -1
        print('{} - {} = {}'.format(t, c, s))
elif p == 2:
    for c in range(10, 0, -1):
        s = c * t
        print('{} * {} = {}'.format(t, c, s))
else:
    print('Opção INVÁLIDA!')
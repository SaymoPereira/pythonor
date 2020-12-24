s = n = count = 0

n = int(input('Digite um número [999 para parar]:'))

while n != 999:
    n = int(input('Digite um número [999 para parar]:'))
    s += n
    count += 1
print(f'Você digitou {n} números, a soma entre eles foi {s}')
print('Fim')
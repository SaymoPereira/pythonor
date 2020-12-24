val = []
im = []
par = []
for c in range(1, 8):
    n = int(input('Digite um número inteiro:'))

    if n % 2 == 0:
        par.insert(c, n)
    else:
        im.insert(c, n)

im.sort()
par.sort()
val.append(im[:])
val.append(par[:])
print(f'Os pares são {val[1]} os impares são {val[0]}')

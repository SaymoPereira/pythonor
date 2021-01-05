#  Tuplas

pessoa = ('Saymo', 17, 'M', 70.5)
del(pessoa)  # Apaga determinada variavel
print(pessoa)

#  lanche = 'Hambúrger', 'Suco', 'Pizza', 'Pudim'

# print(sorted(lanche))  # Mostra em ordem

'''a = (2, 4, 5)
b = (5, 8, 9, 2)
c = b + a #  !=
d = a + b'''

# print(c.index(8))  # Mostra em que posição está determinada coisa

# print(c.count(5))  # Quantas vezes o elemento aparece


'''print(lanche[1])
print(lanche[3])
print(lanche[-2])  # Escreve ao contrário
print(lanche[1:3])  # O 3 é ignorado
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])'''

# print(len(lanche)) conta

'''for cont in range(0, len(lanche)):
    print(f'Comi muito {lanche[cont]}')
print('='*12)
for pos, comida in enumerate(lanche):
    print(f'Comi {comida} na posição {pos}')
for comida in lanche:
    print(f'Comi {comida}')'''
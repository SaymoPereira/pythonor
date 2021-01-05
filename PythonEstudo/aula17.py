'''num = [2, 6, 9, 1]
#  num[2] = 3
num.append(7)
# num.sort()
# num.sort(reverse=True)

num.pop(1)
num.insert(2, 0)  # Insere um número em qualquer posição, basta informar o primeiro paramêtro
num.remove(9)  # Exclui  o primeiro valor setado que achar
print(f'Essa lista {num} tem {len(num)} elementos')'''

valores = list()  # Cria uma lista

'''valores.append(5)
valores.append(9)
valores.append(4)

print(valores)'''

'''for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')'''

a = [1, 2, 3, 4]
b = a
c = a[:]  # Cria uma cópia
print(f'Lista A: {a}\n'
      f'Lista B: {b}\n'
      f'Lista C: {c}')
b[2] = 8
print(f'Lista A: {a}\n'
      f'Lista B: {b}'
      f'Lista C: {c}')


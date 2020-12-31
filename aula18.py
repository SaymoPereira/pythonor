'''teste = list()
teste.append('Saymo')
teste.append(17)
galera = list()
galera.append(teste[:])  # Cria uma cópia da lista teste
teste[0] = 'Maria'
teste[1] = 15
galera.append(teste[:])
print(galera)'''

'''galera = [['João', 15], ['Paulo', 78], ['Iasmin', 45], ['Klara', 12]]
print(galera)
print(galera[2][0])
print(galera[3])
print(galera[0][1])

for p in galera:
    print(f'{p[0]} tem {p[1]} idades')'''
galera = []
dado = []
mai = men = 0
for c in range(0, 3):
    dado.append(input('Digite o nome:'))
    dado.append(int(input('Digite a idade:')))
    galera.append(dado[:])
    dado.clear()  # Limpa os dados

# print(galera)

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade!')
        mai += 1
    else:
        print(f'{p[0]} é menor de idade!')
        men += 1
print(f'Temos {mai} de idade e {men} menores!')
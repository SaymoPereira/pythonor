num = int(input('Digite um número inteiro:'))
print('Escolha uma base para conversão:\n'
      '[1] para Binário\n'
      '[2] para Octal]\n'
      '[3] para Hexadécimal')
opcao = int(input('Sua opção:'))

# Convertendo para diferentes sistemas de números

if opcao == 1:
    print(f'O número {num} em binário é: {bin(num)[2:]}')
elif opcao == 2:
    print(f'O número {num} em Octal é: {oct(num)[2:]}')
elif opcao == 3:
    print(f'O número {num} em Hexadécimal é {hex(num)[2:]}')
else:
    print('Opção inválida!')
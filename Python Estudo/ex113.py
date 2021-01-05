def leiaInt(inteiro):
    while True:
        try:  # Tenta Ler um número convertendo para int
            n = int(input(inteiro))
        except (ValueError, TypeError):  # Dá erro caso exista incompatibilidade de tipos EX 'dois'
            print('Erro! Digite um número INTEIRO válido!')
            continue  # Faz o laço se repetir
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida!')
            return 0
        else:  # Retorna o valor, caso consiga converter para o tipo desejado!
            return n


def leiaReal(real):
    while True:
        try:
            n = float(input(real))
        except (ValueError, TypeError):
            print('Erro! Digite um número REAL válido!')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida!')
            return 0
        else:
            return n


i = leiaInt('Digite um número INTEIRO:')
r = leiaReal('Digite um número REAL:')
print(f'O número inteiro digitado foi {i} e o real {r}')

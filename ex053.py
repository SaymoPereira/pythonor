f = input('Digite uma frase:').strip().upper()
palavras = f.split()  # Separa as palavras(1° função)
junto = ''.join(palavras)
inverso = junto[::-1]

# OU

'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''

if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não é um palindromo')

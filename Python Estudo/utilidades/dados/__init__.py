def leiaDinheiro(preco):
    valido = False

    while not valido:
        entrada = input(preco).replace(',', '.').strip()  # Muda virgula para ponto

        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: "{entrada}" é um preço válido!\033[m')
        else:
            valido = True
            return float(entrada)

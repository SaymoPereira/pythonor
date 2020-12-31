def leiaint(num):
    while True:
        if type(num) != type(int):
            print('Erro! Digite um número inteiro.')
        else:
            print(f'O número escrito foi {num}')


leiaint(int(input()))
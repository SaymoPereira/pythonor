from time import sleep


def maior(* lst):
    print('-='*30, '\nAnalisando valores passados...')
    sleep(1)
    for c in lst:
        print(f'{c}', end=' ')
    print(f'Foram informados {len(lst)} no total'
          f'\nO valor máximo passado foi {max(lst)}')

    print('-='*30)


maior(9, 5, 4, 8, 2, 3)
maior(9, 5, 4, 8, 2, 3, 456,4)

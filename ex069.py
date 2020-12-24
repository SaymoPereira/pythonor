idade = cont = sex = sexf = 0


while True:
    print('-'*20, '\nCadastre uma pessoa\n', '-'*20)

    idade = int(input('Digite a Idade:'))

    resp = sexo = ' '
    while sexo not in 'mf':
        sexo = input('Digite o sexo:').strip().lower()[0]

    if idade >= 18:
        cont += 1
    if sexo == 'm':
        sex += 1
    if sexo == 'f' and idade < 20:
        sexf += 1

    while resp not in 'sn':
        resp = input('Quer continuar? [S/N]')

    if resp == 'n':
        break

print(f'Total de pessoas com mais de 18 anos é {cont}\n'
      f'Ao todo temos {sex} homens cadastrados\n'
      f'E temos {sexf} mulher(es) com menos de 20 cadastradas')
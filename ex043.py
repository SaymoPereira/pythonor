alt = float(input('Digite sua altura (M):'))
pes = float(input('Digite seu peso (Kg):'))

imc = pes / (alt ** 2)

if imc < 18.5:
    print('Seu IMC é {:.2f} você está abaixo do peso!'.format(imc))
elif imc <= 25:
    print('Seu IMC e {:.2f} você está no peso ideal'.format(imc))
elif imc <= 30:
    print('Seu IMC é {:.2f} você está acima do peso!'.format(imc))
else:
    print('Seu IMC é {:.2f} você está obeso!'.format(imc))
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))

media = (n1 + n2)/2

if media >= 7:
    print('Parabéns, você tirou média {} é um aluno explar!'.format(media))
elif media >= 5:
    print('Você tirou media {} está de recuperação'.format(media))
else:
    print('Você foi muito mal, teve média {} esta reprovado!'.format(media))

# Estruturas de controle(aninhadas)
nome = input('Qual o seu nome?').strip()
n1 = int(input('Digite a primeira nota:'))
n2 = int(input('Digite a segunda nota:'))

media = (n1 + n2)/2

if media >= 9:
    print('Parabéns {}, você tirou média {} é um aluno explar!'.format(nome, media))
elif media >= 6:
    print('Parabéns {}, você tirou media {} consegui passar'.format(nome, media))
else:
    print('{} você foi muito mal, teve média {} tente melhorar na próxima!'.format(nome, media))

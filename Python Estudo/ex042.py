r1 = float(input('Digite o primeiro segmento:'))
r2 = float(input('Digite o segundo segmento:'))
r3 = float(input('Digite o terceiro segmento:'))

if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r2 + r1:
      print('Os segmentos podem formar triâgulos ele é um', end=' ')
      if r1 == r2 == r3:
          print('Triângulo equilátero!')
      elif r1 != r2 != r3 != r1:
          print('Triângulo escaleno!')
      else:
          print('Triângulo isósceles!')
else:
    print('Não pode ser um triângulo')
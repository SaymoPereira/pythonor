r1 = float(input('Digite o primeiro segmento:'))
r2 = float(input('Digite o segundo segmento:'))
r3 = float(input('Digite o terceiro segmento:'))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r2 + r1:
    print('Os segmentos podem formar triâgulos')
else:
    print('Os segmentos não podem formar triângulos')

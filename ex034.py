s = float(input('Digite seu salário: '))

if s > 1.250:
    ns = s + (s * 10 / 100)
    print('Seu salário antigo era {:.2f} seu novo é {}'.format(s, ns))
else:
    ns = s + (s * 15 / 100)
    print('Seu salário antigo era {:.2f} seu novo é {:.2f}'.format(s, ns))

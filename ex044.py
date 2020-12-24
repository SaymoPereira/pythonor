from time import sleep
pag = float(input('Digite o preço do produto:'))
f = input('Digite a forma de pagamento:').strip()
f.islower()

if f in 'dinheiro cheque':
    print('Processando...')
    sleep(3)
    print('Total a pagar será R$ {:.2f} você recebeu um desconto de {:.2f}'.format(pag - pag*(10/100), pag*(10/100)))
elif f in 'cartão cartao':
    t = int(input('Digite o total de parcelas, 1 caso o produto seja a vista!'))
    print('Processando...')
    sleep(3)
    if t == 1:
        print('Total a pagar será R$ {:.2f} você recebeu um desconto de {}'.format(pag - pag * (5 / 100), pag * (5 / 100)))
    elif t == 2:
        print('Total a pagar será R$ {:.2f}'.format(pag))
    else:
        print('Total a pagar será R$ {:.2f} com juros de {}'.format(pag + pag * (20 / 100), pag * (20 / 100)))
else:
    print('Erro! Opção não encontrada digite novamente!')
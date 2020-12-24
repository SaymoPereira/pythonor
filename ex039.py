from datetime import date
at = date.today().year

nas = int(input('Digite seu ano de nascimento:'))

c = at - nas

if at-nas == 18:
    print(f'Você tem {c} stá na hora de fazer seu alistamento')
elif at-nas < 18:
    v = 18 - c
    print(f'Você tem {c} anos sinto muito, você ainda não pode se alistar você poderá alistar-se em {v} anos')
else:
    v = c - 18
    print(f'Você tem {c} passou {v} do tempo de alistamento')

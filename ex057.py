sexo = input('Digite seu sexo [M/F]:').strip().upper()[0]
while sexo not in 'F M':
    sexo = input('Dados inválidos, Por Favor informe seu sexo:').strip().lower()[0]
print(f'Sexo {sexo} registrado com sucesso!')
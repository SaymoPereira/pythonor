#  Tratamento de erros e excessões
try:
    a = int(input('Numerador:'))
    b = int(input('Denominador:'))
    r = a / b
#except:
 #   print('Erro! :(')
except Exception as erro:  # Metódo para tratar erro(Exception) e jogar dentro da var(erro)
    print(f'Problema encontrado foi {erro.__class__}')
except (ValueError, TypeError):
    print(f'Tivemos um erro com os tipos de dados passados!')
except ZeroDivisionError:
    print(f'Não é possível dividir por Zero!')
except KeyboardInterrupt:
    print('Você não informou os dados!')
else:
    print(f'Resultado é {r}')
finally:
    print('Volte sempre!')
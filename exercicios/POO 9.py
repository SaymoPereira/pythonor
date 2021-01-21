from classPOO9 import cliente

cliente1 = cliente('Saymo', 17)
cliente1.insereEndereco('Piquet Careneiro', 'CE')
print(cliente1.nome)
cliente1.listaEndereco()

print()

cliente2 = cliente('Alberte', 17)
cliente2.insereEndereco('Salvador', 'BA')
cliente2.insereEndereco('Jeri', 'CE')
print(cliente2.nome)
cliente2.listaEndereco()

print()

cliente3 = cliente('José', 45)
cliente3.insereEndereco('Manaus', 'AM')
print(cliente3.nome)
cliente3.listaEndereco()
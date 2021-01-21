import re

string = 'Esse é um teste de expressões regulares, teste.'

print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'ACSDAS', string))

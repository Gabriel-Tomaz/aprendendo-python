# =========Desafio 22==========
# Manipulando nome do usuario

name = input('Qual seu nome?')
name_array = name.split(' ')

print('Seu nome é maiusculo é {}'.format(name.upper()))
print('Seu nome em minusculo é {}'.format(name.lower()))
print('Seu nome tem {} caracteres'.format(len(name.replace(' ',''))))
print('Seu primeir nome tem {} caracteres'.format(len(name_array[0])))
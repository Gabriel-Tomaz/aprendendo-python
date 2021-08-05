# =========Desafio 22==========
# Mostrando as unidades de um número

number = int(input('Informe um número: '))

unity = number%10 // 1
ten = number%100 // 10
hundred = number%1000 // 100
thousand = number%10000 // 1000

print('Unidade: {}'.format(unity))
print('Dezena: {}'.format(ten))
print('Centena: {}'.format(hundred))
print('Milhar: {}'.format(thousand))

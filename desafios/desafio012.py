# =========Desafio 12==========
# Desconto de 5%

value = float(input('Qual o valor da compra em que será aplicado o desconto ? R$'))

discount = value * 0.05
final = value - discount

print('O valor com desconto é R${:.2f}'.format(final))
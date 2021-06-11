# =========Desafio 7==========
# Média aritmétrica

title = 'Desafio 7'
print('{:=^20}'.format(title))

note1 = float(input('Qual a primeira nota ? '))
note2 = float(input('Qual a segunda nota ? '))
note3 = float(input('Qual a terceira nota ? '))

avarage = (note1 + note2 + note3) / 3

print('Sua média é {:.2f}'.format(avarage))
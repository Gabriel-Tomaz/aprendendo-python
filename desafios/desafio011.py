# =========Desafio 11==========
# Pintura da parede
# uma lata pinta 2m²

width = float(input('Qual a largura da parede ? '))
height = float(input('Qual a altura da parede ?  '))

area = largura * altura
ink = area / 2

print('Para pintar uma parde de {}m²\nVocê precisa de {}L de tinta'.format(area,ink))
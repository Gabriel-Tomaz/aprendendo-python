# =========Desafio 17==========
# Cálculo da Hipotenusa 

from math import pow, sqrt

a = float(input("Qual o comprimento do cateto oposto ? "))
b = float(input("Qual o comprimento do cateto adjacente ? "))

c = pow(a,2) + pow(b,2)

h = sqrt(c)

print("O valor da hipotenusa é {}".format(h))
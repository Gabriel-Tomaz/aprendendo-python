# =========Desafio 17==========
# Seno, Cosseno e tangente

from math import cos,sin,tan,radians

angle = int(input("Informe o ângulo: "))

#Converte o ângulo de graus para radianos.
new_angle = radians(angle)

print("O seno de {} é {:.2f}".format(angle, sin(new_angle)))
print("O cosseno de {} é {:.2f}".format(angle, cos(new_angle)))
print("A tangente de {} é {:.2f}".format(angle,tan(new_angle)))

# =========Desafio 20==========
# Embaralhando nomes

import random

name1 = str(input("Infome o primeiro aluno: "))
name2 = str(input("Infome o segundo aluno: "))
name3 = str(input("Infome o terceiro aluno: "))
name4 = str(input("Infome o quarto aluno: "))

names = [name1,name2,name3,name4]

sort = random.shuffle(names)

print("A ordem de saida é: ")
print(names)
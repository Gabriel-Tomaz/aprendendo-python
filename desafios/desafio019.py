# =========Desafio 19==========
# Sorteio de alunos

import random

name1 = str(input("Infome o primeiro aluno: "))
name2 = str(input("Infome o segundo aluno: "))
name3 = str(input("Infome o terceiro aluno: "))
name4 = str(input("Infome o quarto aluno: "))

names = [name1,name2,name3,name4]

sort = random.choice(names)

print("O vencedor do sorteiro é {}".format(sort))
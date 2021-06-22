# =========Desafio 15==========
# Aluguel de carros

days = int(input("Quantos dias você passou com o carro ? "))
km = float(input("Quantos km foram rodados ? "))

daysValue = days * 60
kmValue = km * 0.15

result = daysValue + kmValue

print("O valor do aluguel é R${}".format(result))
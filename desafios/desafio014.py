# =========Desafio 14==========
# Conversor de temperaturas

temp = float(input("Qual a temperatura atual ? °C: "))

#Novo valor em  fahrenheit
newTempF = (temp * 9/5) + 32

#Novo valor em  Kelvin
newTempK = temp+273.15

print("A temperatura em fahrenheit é {}°F".format(newTempF))
print("A temperatura em Kelvin é {}°K".format(newTempK))
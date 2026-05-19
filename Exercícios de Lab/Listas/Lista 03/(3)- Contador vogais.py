# Crie um programa que receba uma string como argumento e retorne o número de vogais (a, e, i, o, u) que ela contém. 
# O programa deve funcionar tanto para maiúsculas quanto para minúsculas.

frase = input("Informe uma frase para descobrir quantas vogais ela tem: ").upper()
vogais = "AEIOU"
count_vogal = 0

for i in frase:
    if i in vogais:
        count_vogal += 1
print(f"{frase} tem {count_vogal} vogais")
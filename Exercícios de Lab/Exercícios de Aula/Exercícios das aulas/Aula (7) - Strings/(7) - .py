frase = input().upper()
vogais = "AEIOU"
cons = "BCDF..."

count_carac = 0
count_vogal = 0
count_cons = 0

for i in range(frase): 

    qntd_carac = len(frase)

    if frase[i] in vogais:
        count_vogal += 1
    elif frase[i] in cons:
        count_cons += 1

print(f"Vogais = {vogais} \nConsoantes = {cons} \nCaracteres = {qntd_carac} ")
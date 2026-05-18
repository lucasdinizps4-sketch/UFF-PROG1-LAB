# Peça ao usuário para inserir uma frase. O programa deve analisar a frase e exibir as
# seguintes informações:

# O número total de caracteres (incluindo espaços).
# O número de vogais.
# O número de consoantes.

frase = input("\nInforme uma frase: ").upper()
vogais = "AEIOU"
count_vogal = 0
consoante = "BCDFGHJKLMNPQRSTVWXYZ"
count_cons = 0
carac = 0

for i in frase:
    carac += 1
    if i in vogais:
        count_vogal += 1
    elif i in consoante:
        count_cons += 1

print(f"\nQuantidade de caracteres = {carac} \nQuantidade de vogais = {count_vogal} \nQuantidade de consoantes = {count_cons}")
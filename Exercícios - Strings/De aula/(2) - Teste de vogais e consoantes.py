# escreva um programa para ler uma string e verificar se após uma vogal existe uma consoante

frase = "Lucas Diniz".upper()
vogais = "AEIOU"
consoantes = "BCDFGHJKLMNPQRSTVWXYZ"

for i in range(len(frase)-1):
    if frase[i] in vogais:
        if frase[i+1] in consoantes:
            print(f"Depois da vogal {frase[i]} existe uma consoante")

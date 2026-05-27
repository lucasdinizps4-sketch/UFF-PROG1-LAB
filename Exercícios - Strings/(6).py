# Escreva um programa para contar quantas letras a ocorre em uma String.

s = input("Informe uma frase")
count_a = 0
for i in s:
    if i == "a":
        count_a += 1
print(f"Números de 'a': {count_a} em {s}")
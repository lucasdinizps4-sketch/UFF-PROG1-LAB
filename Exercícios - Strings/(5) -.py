# Escreva um programa para calcular a soma e a média dos algarismos presentes em uma string.

contador = 0 
soma = 0

s1 = input("Informe uma frase")

for i in s1:
    if i.isnumeric():
        contador += 1
        soma += int(i)

print(f"Soma é = {soma} \nMédia = {soma/contador}")
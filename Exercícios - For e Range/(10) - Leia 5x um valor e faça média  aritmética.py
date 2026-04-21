# Escreva um programa que leia 5 valores inteiros, um de cada vez, e calcule a média aritmética dos números lidos.

soma = 0
cont = 0
for i in range(5):
    N = int(input("Informe valor de N: "))
    soma = soma + N
    cont = cont + 1
    
media = soma/cont

print(f"Média: {media}")


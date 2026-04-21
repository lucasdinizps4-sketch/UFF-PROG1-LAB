# Escreva um programa que leia 5 valores inteiros, um de cada vez e calcule a soma deles.

soma = 0 
for i in range(5):
    N = int(input("Informe valor de N: "))
    soma = soma + N
print(f"O somátorio de N é: {soma}")
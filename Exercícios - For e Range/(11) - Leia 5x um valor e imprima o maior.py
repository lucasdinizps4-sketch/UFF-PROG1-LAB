# Escreva um programa que leia 5 valores inteiros, um de cada vez. Encontrar e escrever o maior valor lido.

maior = int(input("Informe um valor: "))
menor = maior

for i in range(5):
    N = int(input("Informe o valor de N: "))
    if N > maior:
        maior = N
    elif N < menor:
        menor = N
    print(f"Maior = {maior}")
    print(f"Menor = {menor}")


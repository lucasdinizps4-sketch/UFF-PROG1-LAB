# Somatório de n números: Vamos criar um programa que some n números inteiros e imprima o resultado da soma.

N = 0
soma = 0

while True:
    N = int(input("Informe valor de N: "))
    if N<=0:
        break
    soma = soma + N 

print(f"Soma é {soma}")


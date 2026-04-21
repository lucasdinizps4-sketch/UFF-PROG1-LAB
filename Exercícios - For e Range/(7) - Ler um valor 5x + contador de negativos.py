# Escrever um programa que leia 5 valores, um de cada vez, e conta quantos destes valores são negativos.
contador_neg = 0
for i in range(5):
    N = int(input("Informe valor de N: "))
    if N < 0:
        contador_neg = contador_neg + 1
        print(f"Quantidade de negativos: {contador_neg} ")

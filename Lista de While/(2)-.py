# Escreva um programa para somar um conjunto de números pares fornecidos pelo usuário. A finalização do conjunto de dados termina quando o usuário
# digitar 0. Considere que números ímpares também podem ser fornecidos na entrada. 

n = 1
soma_par = 0

while n != 0:
    n = int(input("Informe valor de N: "))
    if n % 2 == 0:
        soma_par += n
    else: 
        print("Número ímpar!")

print(f"Soma dos pares = {soma_par}")
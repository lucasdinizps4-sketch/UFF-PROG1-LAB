# Escreva um programa para ler vários valores inteiros e calcular a média de uma sequência de números. A finalização do conjunto de dados termina
# quando o usuário digitar 0.

n = 1 
count = 0 
soma = 0

while n != 0:
    if n == 0:
        break
    n = int(input("Informe N: "))
    soma += n
    count += 1

media = soma / count
print(f"Média = {media:.2f}")



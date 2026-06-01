# Escreva um programa para ler vários valores inteiros e calcular a média de uma sequência de números. A finalização do conjunto de dados termina
# quando o usuário digitar 0 ou quando a média for maior 3.0.

n = 1
media = 0
count = 0
soma = 0

while n != 0 and media <= 3.0:
    n = int(input("Informe N: "))
    count += 1
    soma += n 
    media = soma / count
    print(f"Media = {media}")


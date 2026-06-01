# Escreva um programa que leia uma sequência de valores inteiros, a finalização do conjunto de dados termina quando o usuário digitar 0, e:
# a) imprima todos os números; ok
# b) imprima o maior e o menor valor.


n = 1
maior = float("-inf")
menor = float("+inf")

while n != 0:
    n = int(input("Nforme valor de N: "))
    if n == 0:
        break
    print(n)
    if n > maior:
        maior = n
    elif n < menor and n != maior: 
        menor = n
print(f"Maior = {maior} \nMenor = {menor}")



# Dada a lista numeros = [12, -5, 23, 4, 18, 9, 27, 10, -1], escreva um programa que crie
# uma nova lista contendo apenas os números que são maiores que 10. Ao final, imprima a nova lista.

numeros = [12,-5,23,4,18,9,27,10,-1]
nova_lista = []

for i in range(len(numeros)):
    if numeros[i] > 10:
        nova_lista.append(numeros[i])

print(nova_lista)
# 5) Dada uma lista com elementos duplicados, como minha_lista = [1, 2, 2, 3, 4, 4, 5, 1],
# escreva um programa que crie uma nova lista contendo apenas os elementos únicos da lista original, sem repetições. A nova lista deve ser [1, 2, 3, 4, 5].



minha_lista = [1,2,2,3,4,4,5,1]
nova_lista = []

for i in range(len(minha_lista)):
    if minha_lista[i] not in nova_lista:
        nova_lista.append(minha_lista[i])

print(nova_lista)

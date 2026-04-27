
# Dadas duas listas de mesmo tamanho, crie um programa que gere uma terceira lista contendo os elementos das duas listas originais intercalados.

lista_c = []
lista_a = ["a", "c", "e"]
lista_b = ["b", "d", "f"]

for i in range(len(lista_a)):
    lista_c.append(lista_a[i])
    lista_c.append(lista_b[i])

print(lista_c)


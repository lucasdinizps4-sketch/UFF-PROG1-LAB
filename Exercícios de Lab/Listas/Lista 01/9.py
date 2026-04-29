lista =[]
lista_invertida = []
for i in range(5):
    convidado = input(f"Informe o nome do convidado {i+1}: ")
    lista.append(convidado)

for i in range(len(lista)):
    lista_invertida.insert(0, lista[i])

print(f"Lista original: {lista_invertida}")




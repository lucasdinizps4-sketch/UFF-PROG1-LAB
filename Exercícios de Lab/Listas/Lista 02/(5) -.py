minha_lista = [1,2,2,3,4,4,5,1]
nova_lista = []

for i in range(len(minha_lista)):
    if minha_lista[i] not in nova_lista:
        nova_lista.append(minha_lista[i])

print(nova_lista)

# Rescreva o programa abaixo que exclui o primeiro elemento da lista com valor especificado, mas utilizando uma função.

lista = [1, 4, 5, 6, 4, 7]
valor = 4
removeu = False
temp = []
for i in range(len(lista)):
    if lista[i] != valor or removeu:
        temp.append(lista[i])
    else:
        removeu = True
lista = temp
print(lista)

# -----------------------------------------

def exc_primeiro(lista,n):
    removeu = False
    temp = []
    for i in range(len(lista)):
        if lista[i] != n or removeu:
            temp.append(lista[i])
        else:
            removeu = True
    lista = temp
    return lista

numeros = [1,2,3,4,1,5,4]

print(exc_primeiro(numeros,1))






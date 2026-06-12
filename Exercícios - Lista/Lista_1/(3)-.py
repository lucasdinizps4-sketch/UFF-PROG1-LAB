# Rescreva o programa abaixo que exclui um elemento da lista em uma determinada posição e obter o valor excluído, mas utilizando uma função. 

lista = [1, 2, 3, 4]
pos = 2
elementoRetirado = 0
temp = []
for i in range(len(lista)):
    if i != pos:
        temp.append(lista[i])
    else:
        elementoRetirado = lista[i]
lista = temp
print(lista)
print(elementoRetirado)

# -------------------------------------

def receber_val_remov(lista,pos):
    elemento_retirado = 0
    temp = []
    for i in range(len(lista)):
        if i != pos:
            temp.append(lista[i])
        else:
            elemento_retirado = lista[i]
    lista = temp
    return lista,elemento_retirado


numeros = [0,1,3,4,5,8]
pos_removida = int(input(f"Qual posição você quer remover? (De 0 até {len(numeros)-1}): "))

nova_list,elementoretirado = receber_val_remov(numeros,pos_removida)

print(nova_list)
print(f"lemento retirado: {elementoretirado}")
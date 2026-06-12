# Rescreva o programa abaixo que procure em uma lista um valor fornecido e retorne posição onde ele foi encontrado ou -1 caso não esteja na lista, mas
# utilizando uma função

lista = [1, 2, 10, 5, 20]
valor = 10
pos = -1
for i in range(len(lista)):
    if lista[i] == valor:
        pos = i
print(pos)

# ------------------------------

def proc_valor(lista,n):
    pos = -1
    for i in range(len(lista)):
        if lista[i] == n:
            pos = i
    return pos

numeros = [1,2,3,4,5,6,7,8,9]
n_procurado = int(input("Informe o valor que você deseja procurar: "))

if proc_valor(numeros,n_procurado) == -1: 
    print(f"Número não está na lista!")
else:
    print(f"{n_procurado} está na posição: {proc_valor(numeros,n_procurado)}")
# Peça ao usuário para digitar 6 números inteiros e guarde-os em uma lista chamada numeros. Depois, use um loop for para criar duas listas novas:

# pares: apenas os números pares da lista original.

# impares: apenas os números ímpares da lista original.

# Ao final, imprima as três listas.

numeros = []
numeros_par = []
numeros_impar = []

for i in range(6):
    n1 = int(input("Informe um número: "))
    numeros.append(n1)

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        numeros_par.append(numeros[i])
    else:
        numeros_impar.append(numeros[i])

print(f"Números: {numeros} \nNúmeros par: {numeros_par} \nNúmeros ímpar: {numeros_impar}")
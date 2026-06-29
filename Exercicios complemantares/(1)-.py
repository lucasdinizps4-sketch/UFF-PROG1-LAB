# Escreva um programa que forneça a média aritmética dos elementos de uma lista simplesmente

def media_arit(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma / len(lista)

minha_lista = [1,3,7,8,23,80]
print(f"Média = {media_arit(minha_lista):.1f}")
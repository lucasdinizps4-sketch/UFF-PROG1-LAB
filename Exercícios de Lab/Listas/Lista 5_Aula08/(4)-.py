# Escreva uma função na linguagem Python que receba uma matriz (lista de listas) de
# números e retorne os números máximo e mínimo desta matriz. Use estruturas de repetição.

matriz = [[10,30],[458,3],[58,-20]]

def max_min(matriz):
    maior = matriz[0][0]
    menor = maior
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maior: 
                maior = matriz[i][j]
            elif matriz[i][j] < menor:
                menor = matriz[i][j]
    return maior,menor

print(max_min(matriz))
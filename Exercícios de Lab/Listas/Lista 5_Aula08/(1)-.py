# Escreva uma função em Python que receba uma lista de números e retorne o maior número presente no lista.

lista = [40,20,35,-2,25,80]

def achar_maior(lista):
    maior = lista[0]
    menor = maior
    
    for i in range(1,len(lista)):
        if lista[i] > maior:
            maior = lista[i]
        if lista [i] < menor:
            menor = lista[i]
    return maior,menor

print(achar_maior(lista))
# Escreva em Python uma função chamada iguais(L1, L2) que receba duas listas como parâmetros e retorne um valor lógico:

# Verdadeiro (True), se as listas forem exatamente iguais (mesmo tamanho e mesmos elementos na mesma ordem).
# Falso (False), caso contrário.

def iguais(l1,l2):
    if len(l1) != len (l2):
        return False
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True


lista1 = [1,2,3,4,5,6]
lista2 = [1,2,3,4,5,6]
lista3 = [1,2,3,4,5,7]

print(f"Comparando lista1 e lista2: {iguais(lista1,lista2)}") 
print(f"Comparando lista2 e lista3: {iguais(lista2,lista3)}")
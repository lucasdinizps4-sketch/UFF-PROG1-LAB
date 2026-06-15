def criar_lista(qntd):
    a = []
    for _ in range(qntd):
        n = int(input("Informe um número: "))
        a.append(n)
    return a

# Faça um programa em Python para ler, por meio de uma função, uma lista a de elementos inteiros e calcule e imprima o valor de S, sendo:

def somatorio(a):
    s = 0
    contador = 0
    for i in range(len(a)):
        numerador = i
        s += numerador / a[i]
        if numerador <= a[i]:
            contador += 1

    return s,contador








# Dados 5 pares de valores inteiros a e b, distintos entre si, escreva um programa para imprimir o maior de cada par.

for i in range(5):
    a = int(input("Informe A: "))
    b = int(input("Informe B: "))
    
    if a == b:
        print("A e B não podem ser iguais")
    elif a > b: 
        print(f"O maior é {a}")
    else: 
        print(f"O maior é {b}")
    

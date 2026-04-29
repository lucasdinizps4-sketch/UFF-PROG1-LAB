# Peça ao usuário um número inteiro N. Escreva um programa que gere e imprima os N primeiros termos da sequência de Fibonacci. A sequência começa com 0 e 1, e cada termo
# subsequente é a soma dos dois anteriores (ex: 0, 1, 1, 2, 3, 5, 8, ...).



n = int(input())
if n <1:
    print("Número inválido")
elif n == 1:
    print("[0]")
else:
    fib = [0,1]
    for i in range(n):
        fib.append(fib[i] + fib[i+1])
print(fib)

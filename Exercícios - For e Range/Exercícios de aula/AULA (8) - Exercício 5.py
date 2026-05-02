# Escrever um programa que gere e imprima os números de 1 até 10. Observe que não há leitura de valores.

for i in range(11):
    if i % 2 == 0:
        print(i)

# OU

for i in range(0,11,2): # Começa de 0 e vai até 10 de 2 em 2
    print(i)
# Faça um programa que leia 15 números inteiros, um de cada vez, e calcule o somatório desses números.

soma = 0 # Variável vazia, para acumular no loop

for i in range(15):
    n = int(input(f"Informe o número {i+1}: ")) # [i+1] para o programar informar quantos números já foram recebidos, (range começa em 0, logo i+1 me retorna 1)
    soma = soma + n # Starta com N informado pelo úsuário e somando + soma (0), com isso ele acumula os valores
    print(f"Soma de {n} + {soma-n} é = {soma}") # {soma-n} para ele imprimir com qual número N está somando, 10 + 0 , soma passa valar de 10, 10-10(soma-n) = 0. Logo ele me mostra 10+0=10. Segundo loop, N é 20, 20+10 = 30 (soma = soma + n), 30-20 = 10, logo (soma-n = 10).
print(f"Soma total = {soma}")


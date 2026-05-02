# Faça um programa que leia 25 números inteiros e calcule o somatório dos números pares e ímpares lidos. 


soma_par = 0
soma_impar = 0

for i in range(8):
    n = int(input(f"Informe o número {i+1}"))
    if n % 2 == 0: 
        soma_par += n # Variável += n ----> Variável = Variável + n
    elif n % 2 != 0:
        soma_impar += n
print(f"Soma dos números ímpares = {soma_impar}")
print(f"Soma dos números pares = {soma_par}")



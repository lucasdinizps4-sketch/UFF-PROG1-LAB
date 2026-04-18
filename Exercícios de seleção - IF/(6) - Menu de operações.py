# Faça um programa que mostre o menu de opções a seguir, receba a opção do usuário e os dados necessários para executar cada operação.

# Menu de opções:
# 1. Somar dois números.
# 2. Raiz quadrada de um número.
# Digite a opção desejada:

import math

menu = input("Bem vindo ao menu de opções!\n As opções são:\n (1) - Somar 2 números\n (2) - Raiz quadrada de um número! \nEscolha uma opção: ")

if menu == "1": 
    n1 = int(input("\nInforme valor do primeiro número: "))
    n2 = int(input("Informe valor do segundo número: "))
    soma = n1+n2
    print(f"\nA soma de {n1} com {n2} é: {soma}")

else:
    n1 = int(input("\nInforme um número: "))
    raiz = math.sqrt(n1)
    print(f"\nA raiz quadrada de {n1} é: {raiz:.2f}")



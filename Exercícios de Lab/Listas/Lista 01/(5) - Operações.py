# Construa um programa que leia 2 números reais informados pelo usuário. Ao fim, o programa deve calcular e imprimir:
# a) a soma dos dois valores;
# b) o produto entre eles;
# c) a divisão entre eles;
# d) o primeiro número elevado ao quadrado;
# e) a raiz quadrada do segundo número.

import math

n1 = int(input("\nInforme o valor do primeiro número: "))
n2 = int(input("Informe o valor do segundo número: "))

soma = n1+n2
produto = n1*n2
divisao = n1/n2
potencia = n1**2
raiz = math.sqrt(n2)

print(f"\nA soma dos dois valores é = {soma} \nO produto dos dois valores = {produto} \nA divisão entre eles é = {divisao} \n{n1} elevado ao quadrado é = {potencia} \nRaiz quadrada de {n2} é = {raiz:.2f}")


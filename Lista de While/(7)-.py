# Escreva um programa que calcule o máximo divisor comum de dois números.

divisores_de_n = int(input())
divisores_de_n2 = int(input())
lista_n = []
lista_n2 = []


for i in range(1,divisores_de_n+1):
    if divisores_de_n % i == 0:
        lista_n.append(i)

for j in range(1,divisores_de_n2+1):
    if divisores_de_n2 % j == 0:
        lista_n2.append(j)

print(f"Divisores de {divisores_de_n}: {set(lista_n)} \nDivisores de {divisores_de_n2}: {set(lista_n2)}")

print(f"MDC de {divisores_de_n} e {divisores_de_n2}: {set(lista_n) & set(lista_n2)}")


# Solução do professor (bem mais simples)

n1 = int(input("Informe n1: "))
n2 = int(input("Informe n2: "))

while n2 != 0:
    temp = n2
    n2 = n1 % n2
    a = temp 
print(f"DMC = {a}")
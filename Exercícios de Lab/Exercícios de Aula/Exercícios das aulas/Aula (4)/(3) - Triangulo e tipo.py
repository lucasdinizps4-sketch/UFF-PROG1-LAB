# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso
# os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

a = float(input("Informe o lado A do triângulo: "))
b = float(input("Informe o lado B do triângulo: "))
c = float(input("Informe o lado C do triângulo: "))

if (a+b > c) and (c+b > a) and (c+a > b):
    print("É um triangulo")

    if a == b and b == c:
        print("Triângulo Equilátero")
    elif a == b or b == c:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else: 
    print("Não é um triangulo")
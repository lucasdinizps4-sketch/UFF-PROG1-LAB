# Escrever um programa que lê 3 valores a, b, c que são lados de um triângulo e calcule a área deste triângulo. O total de triângulos é igual 55. 
# raiz de s*(s − a)(s − b)(s − c)
# onde s = sem perímetro - S = (A+B+C)/2

import math

for i in range(55):
    a = float(input("\nInforme valor de A: "))
    b = float(input("Informe valor de B: "))
    c = float(input("Informe valor de C: ")) 
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    count = i + 1
    print(f"\nÁrea do triângulo ({count}), é: {area:.1f} ")
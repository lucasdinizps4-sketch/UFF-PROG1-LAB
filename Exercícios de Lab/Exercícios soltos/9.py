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
        a!=b and b!=c and c!=a
        print("Triângulo Escaleno")
    
else: 
    print("Não é um triangulo")
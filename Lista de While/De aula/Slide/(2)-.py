# Para A e B inteiros e maiores que zero, fazer um programa para o cálculo A dividido por B usando subtrações sucessivas.

A = int(input("Digite A: "))
B = int(input("Digite B: "))

quociente = 0

while A >= B:
    A = A - B
    quociente = quociente + 1

print("Quociente:", quociente)
print("Resto:", A)
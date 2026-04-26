# Tabuada de Multiplicação: "Vamos criar um programa que pede um número ao usuário e exibe sua tabuada de 1 a 10. 
n1 = int(input("Informe um número"))

for i in range(1,11):
    multiplicador = n1*i
    print(f"{n1} * {i} = {multiplicador}")
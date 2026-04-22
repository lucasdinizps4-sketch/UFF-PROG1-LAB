# Escreva um programa para ler 40 valores lidos dois a dois, calcular e escrever a média aritmética entre cada par de números. 

for i in range(20):
    n1 = int(input("\nInforme o valor de n1: "))
    n2 = int(input("Informe o valor de n2: "))
    media = (n1+n2)/2
    count = i + 1
    print(f"\nA média aritmética do par {count}, é: {media}")


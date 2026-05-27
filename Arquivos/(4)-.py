# Escreva um programa que leia dois valores inteiros que formarão um intervalo,
# posteriormente, leia um arquivo contendo números inteiros e calcula a soma dos
# números pares compreendidos entre dois números lidos.

superior = int(input("Informe um número: "))
inferior = int(input("Informe outro número: "))

if superior > inferior:
    arquivo = open("Arquivos/numeros.dat", "r", encoding = "utf-8")
    soma_par = 0
    for numero in arquivo:
        numero = numero.strip()
        numeroint = int(numero)
        
        if numeroint >= inferior and numeroint <= superior and numeroint % 2 == 0:
            soma_par += numeroint
    arquivo.close()

    print(f" Soma dos pares = {soma_par}")
else:
    print(f"Fora do limite")

# Escreva um programa que leia uma sequência de valores inteiros, a finalização do conjunto de dados termina quando o usuário digitar 0, e:
# a) imprima todos os números;
# b) imprima o maior número par;

n = 1 
primeiro = True

while n != 0:
    n = int(input("Informe valor de N: "))
    print(n)
    if n % 2 == 0:
        if primeiro:
            maior_par = n
            primeiro = False
        elif n > maior_par:
            maior_par  = n
print(f"Maior par: {maior_par}")
        
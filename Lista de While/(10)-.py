# Dado um intervalo de números inteiros positivos, escreva um programa para contar quantos números inteiros primo há no intervalo.

inicio = int(input("Digite o valor inicial do intervalo: "))
fim = int(input("Digite o valor final do intervalo: "))

contador_primos = 0

for num in range(inicio, fim + 1):
    if num <= 1:
        continue 
        
    eh_primo = True

    for i in range(2, num):
        if num % i == 0:
            eh_primo = False
            break  
    
    if eh_primo:
        contador_primos += 1

print(f"No intervalo de {inicio} até {fim}, existem {contador_primos} números primos")
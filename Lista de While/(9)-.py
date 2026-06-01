# Faça um programa que leia um valor inteiro e verifique se ele é primo. 


num = int(input("Digite um número inteiro: "))

if num <= 1:
    eh_primo = False
else:
    eh_primo = True
    for i in range(2, num):
        if num % i == 0:
            eh_primo = False
            break

if eh_primo:
    print(f"O número {num} é primo")
else:
    print(f"O número {num} não é primo")
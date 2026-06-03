# Par ou Ímpar: Peça ao usuário um número inteiro. Verifique se o número é par ou ímpar e exiba a resposta 

n1 = int(input("Informe um número: "))

if n1 % 2 == 0: 
    print(f"{n1} é par")
else:
    print(f"{n1} é ímpar")
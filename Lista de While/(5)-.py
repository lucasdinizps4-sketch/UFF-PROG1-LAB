# Escreva um programa que leia uma sequência de dados (idade, salário) de pessoas e imprima o total de pessoas com salário maior que R$ 5000,00 e
# idade < 40; a finalização do conjunto de dados termina quando o usuário digitar 0 para a idade.

count = 0
idade= 1
maior = float("-inf")

while idade != 0:
    idade = int(input("Informe idade: "))
    if idade == 0:
        break
    salario = int(input("Informe salário: "))
    if salario > 5000 and idade < 40: 
        if salario > maior:
            maior = salario

if maior == float("-inf"):
    print("Não foi encontrado um salario maior que 5000 e idade menor que 40")
else:
    print(f"O maior salário acima de 5000 e idade menor que 40 foi: \nSalário: {maior}")
    





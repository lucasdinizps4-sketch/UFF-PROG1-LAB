# Faça um programa que receba o salário de um funcionário e usando a tabela a seguir, calcule e mostre o novo salário.
# 300 ---> 50% de aumento ok
# > 300 até 500 ---> 40% de aumento ok
# > 500 até 700 ---> 30% de aumento ok
# > 700 até 800 ---> 20% de aumento ok
# > 800 até 1000 ---> 10% de aumento
# > 1000 ---> 5% de aumento 

salario = float(input("Informe seu salario: "))

if salario <= 300:
    novo_salario = salario + (salario * 0.5)

elif salario > 300 and salario <= 500:
    novo_salario = salario + (salario * 0.4)

elif salario > 500 and salario <= 700:
    novo_salario = salario + (salario * 0.3)

elif salario > 700 and salario <= 800:
    novo_salario = salario + (salario * 0.2)

elif salario > 800 and salario <= 1000:
    novo_salario = salario + (salario * 0.1)

else: 
    novo_salario = salario + (salario * 0.05)

print(f"Seu salario de {salario} reais, agora é de {novo_salario} reais")
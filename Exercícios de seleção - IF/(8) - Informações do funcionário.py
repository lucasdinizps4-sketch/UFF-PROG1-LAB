# Faça um programa que receba o valor do salário mínimo, o número de horas trabalhadas, o número de dependentes do funcionário e a quantidade de horas extras trabalhadas. Calcule e mostre o salário a receber do - 
# funcionário de acordo com as regras a seguir:

# a) O valor da hora trabalhada é igual a 1/5 do salário mínimo.
# b) O salário do mês é igual ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada.
# c) Para cada dependente, acrescentar R$ 32,00. 
# d) Para cada hora extra trabalhada, calcular o valor da hora trabalhada acrescida de 50%.
# e) O salário bruto é igual ao salário do mês mais o valor dos dependentes mais o valor das horas extras.
# f) Calcular o valor do imposto de renda retido na fonte de acordo com atabela a seguir: 

# IRRF , salário bruto
# Isento, < 200
# 10%, >= 200 e <= 500
# 20%, > 500

# g) O salário líquido é igual ao salário bruto menos IRRF.
# h) A gratificação é de acordo com a tabela a seguir:

# Salário líquido, gratificação
# <= 350, 100
# > 350, 50

# i) O salário a receber do funcionário é igual ao salário líquido mais a gratificação.

salario_m = float(input("Informe o salário mínimo:  "))
horas_trabalhadas = float(input("Informe o número de horas trabalhadas: "))
dependentes = int(input("Informe o número de dependentes: ")) * 32
horas_extras = float(input("Informe o número de horas extras: "))

hora_trabalhada1 = salario_m * (1/5)
salario_mes = horas_trabalhadas * hora_trabalhada1
hora_extra1 = (hora_trabalhada1 + (hora_trabalhada1 *0.5)) * horas_extras
salario_bruto = salario_mes + dependentes + hora_extra1

if salario_bruto < 200:
    IRRF = 0
elif salario_bruto >= 200 and salario_bruto <= 500:
    IRRF = salario_bruto * 0.1
elif salario_bruto > 500:
    IRRF = salario_bruto * 0.2

salario_liquido = salario_bruto - IRRF

if salario_liquido <= 350:
    gratificacao = 100 
elif salario_liquido > 350:
    gratificacao = 50

salario_receber = salario_liquido + gratificacao

print(f"\nSeu salário a receber é de: {salario_receber}")
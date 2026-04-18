# Faça um programa que receba o código correspondente ao cargo de um funcionário e seu salário atual e mostre o cargo, o valor do aumento e seu novo salário. Os cargos estão na tabela a seguir.

# Código, cargo, percentual de aumento

# 1, Escriturário, 50%
# 2, Secretário, 35%
# 3, Caixa, 20%
# 4, Gerente, 10%
# 5, Diretor, sem aumento

codigo = input("Informe seu código de identificação: ")
salario = float(input("Informe seu salário: "))

if codigo == "1":
    novo_salario = salario + (salario * 0.5)
    codigo = "Escriturário"

elif codigo == "2":
    novo_salario = salario + (salario * 0.35)
    codigo = "Secretário"

elif codigo == "3":
    novo_salario = salario + (salario * 0.2)
    codigo = "Caixa"

elif codigo == "4":
    novo_salario = salario + (salario * 0.1)
    codigo = "Gerente"

elif codigo == "5":
    novo_salario = salario
    codigo = "Diretor"

print(f"\nCargo: {codigo} \nAumento: {novo_salario - salario} \nNovo salário: {novo_salario} ")


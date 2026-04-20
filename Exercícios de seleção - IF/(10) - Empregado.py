# Faça um programa que receba o valor do salário mínimo, o turno de trabalho (M — matutino; V — vespertino; ou N — noturno), a categoria (O — operário; G — gerente) e o número de horas trabalhadas no mês de um funcionário.
# Suponha a digitação apenas de dados válidos e, quando houver digitação de letras, utilize maiúsculas. Calcule e mostre:

# O coeficiente do salário, de acordo com a tabela a seguir.

# TURNO DE TRABALHO, VALOR DO COEFICIENTE 
# MATUTINO (M), 10% do salario minimo
# VESPERTINO (V), 15% do salario minimo
# NOTURNO (N), 12% do salario minimo

# O valor do salário bruto, ou seja, o número de horas trabalhadas multiplicado pelo valor do coeficiente do salário.

# O imposto, de acordo com a tabela a seguir.

# CATEGORIA, SALARIO BRUTO, IMPOSTO SOB SALARIO BRUTO
# OPERARIO (O), >= 300, 5%
# OPERARIO (O), < 300, 3% 
# GERENTE (G), >= 400, 6%
# GERENTE (G), < 400, 4%

# A gratificação, de acordo com as regras a seguir. Se o funcionário preencher todos os requisitos a seguir, sua gratificação será de R$ 50,00; caso contrário, será de R$ 30,00. Os requisitos são:
# Turno: Noturno
# Número de horas trabalhadas: Superior a 80 horas

# O auxílio alimentação, de acordo com as seguintes regras. Se o funcionário preencher algum dos requisitos a seguir, seu auxílio alimentação será de um terço do seu salário bruto; caso contrário, será de
# metade do seu salário bruto. Os requisitos são:
# Categoria: Operário
# Coeficiente do salário: < = 25

# O salário líquido, ou seja, salário bruto menos imposto mais gratificação mais auxílio alimentação. A classificação, de acordo com a tabela a seguir:
# SALARIO LIQUIDO, MENSAGEM 
# < 350, "MAL REMUNERADO"
# >= 350 e <= 600, "NORMAL"
# > 600, "BEM REMUNERADO"

salario_minimo = float(input("Informe valor do salário mínimo: "))
print("\nOpções de turno de trabalho: \nMatutino (M) \nVespertino (V) \nNoturno (N) \n\nOpções de categoria: \nOperário (O) \nGerente (G) ")

turno = input("\nInforme seu turno: ")
categoria = input("Informe sua categoria: ")
n_horas = float(input("Informe número de horas trabalhadas no mês: "))

if turno == "M":
    coeficiente = salario_minimo * 0.1
elif turno == "V":
    coeficiente = salario_minimo * 0.15
else:
    coeficiente = salario_minimo * 0.12

salario_bruto = n_horas * coeficiente

if categoria == "O" and salario_bruto >= 300:
    imposto = salario_bruto * 0.5
elif categoria == "O" and salario_bruto < 300:
    imposto = salario_bruto * 0.3
elif categoria == "G" and salario_bruto >= 400:
    imposto = salario_bruto * 0.6 
elif categoria == "G" and salario_bruto < 400:
    imposto = salario_bruto * 0.4

if turno == "N" and n_horas > 80:
    gratificacao = 50
else:
    gratificacao = 30

if categoria == "O" or coeficiente <= 25: 
    auxilio_a = salario_bruto * 1/3
else: 
    auxilio_a = salario_bruto / 2

salario_liquido = (salario_bruto - imposto) + gratificacao + auxilio_a 

if salario_liquido < 350:
    print("MAL REMUNERADO")
elif salario_liquido >= 350 and salario_liquido <= 600:
    print("NORMAL")
elif salario_liquido > 600:
    print("BEM REMUNERADO")
          

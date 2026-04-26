# Uma empresa define o bônus de fim de ano com base no percentual de metas que um funcionário atingiu:

# Se atingiu mais de 100% da meta: bônus de 15% do salário.
# Se atingiu entre 80% e 100% (inclusive): bônus de 10% do salário.
# Se atingiu entre 50% e 79% da meta: bônus de 5% do salário.
# Abaixo de 50%: sem bônus.

salario = int(input("Informe salário: "))
meta_atingida = int(input("Informe percentual da meta atingida: "))

if meta_atingida >100:
    novo_salario = salario + (salario * 0.15)
elif meta_atingida >= 80 and meta_atingida <= 100:
    novo_salario = salario + (salario * 0.1)
elif meta_atingida >= 50 and meta_atingida <= 79:
    novo_salario = salario + (salario * 0.05)
else:
    novo_salario = salario

if novo_salario>salario:
    print(f"Você ganhou {novo_salario-salario} reais de bonus.")
else: 
    print("Você não ganhou bonus")
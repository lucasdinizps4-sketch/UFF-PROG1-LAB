# Calculadora de Preço de Ingresso de Cinema

# Preço normal: R$ 30,00.
# Crianças (abaixo de 12 anos) pagam meia: R$ 15,00.
# Idosos (acima de 60 anos) pagam R$ 20,00.
# Estudantes que não são crianças ou idosos também pagam meia: R$ 15,00."

preco_normal = 35
idade = int(input("Informe sua idade: "))
estudante = input("Você é estudante? (s/n): ")

if idade < 12 or estudante == "s":
    novo_preco = 15
elif idade > 60:
    novo_preco = 20
else:
    novo_preco = 35

print(f"Preço do ingresso é: {novo_preco}")
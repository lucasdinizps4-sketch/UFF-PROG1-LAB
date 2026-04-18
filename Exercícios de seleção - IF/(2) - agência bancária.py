# Uma agência bancária possui dois tipos de investimentos, conforme o quadro a seguir. Faça um programa que receba o tipo de investimento e seu valor, calcule e mostre o valor corrigido após um mês de investimento, de
# acordo com o tipo de investimento.

# Tipo 1 , poupança , 3% ao mes
# Tipo 2 , fundos de renda fixa , 4%

print("Tipos de investimento: Poupança (1) e Fundos de renda fixa (2)")

investimento = input("Informe o tipo de investimento que você gostaria (1 ou 2): ")
valor_inv = float(input("Informe o valor que será investido: "))
retorno_p = valor_inv * 0.03
retorno_f = valor_inv * 0.04

if investimento == "1":
    valor_corrigido = valor_inv + retorno_p

else: 
    valor_corrigido = valor_inv + retorno_f

print(f"Seu valor investido foi de {valor_inv}, após um mes você tera um retorno de {valor_corrigido - valor_inv} com valor corrigido de {valor_corrigido}")





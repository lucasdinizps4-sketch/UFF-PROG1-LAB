# Uma loja online precisa calcular o valor do frete de uma entrega com base na região do país informada pelo cliente. Cada região tem um valor de frete fixo.
# Sudeste: R$ 15,00
# Sul: R$ 20,00
# Nordeste: R$ 25,00
# Centro-Oeste: R$ 22,00
# Norte: R$ 30,00

# O programa deve perguntar a região do cliente e informar o valor do frete. Se a região digitada não for válida, o programa deve informar que a entrega não está disponível para
# aquela localidade.

print("Regiões de entrega: \nSudeste \nSul \nNordeste \nCentro-Oeste \nNorte")

regiao = input("Informe sua região: ")

if regiao == "Sudeste":
    frete = 15
    print(f"Frete de {regiao} é: {frete}")
elif regiao == "Sul":
    frete = 20
    print(f"Frete de {regiao} é: {frete}")
elif regiao == "Nordeste":
    frete = 25
    print(f"Frete de {regiao} é: {frete}")
elif regiao == "Centro-Oeste" or regiao == "Centro Oeste": 
    frete = 22
    print(f"Frete de {regiao} é: {frete}")
elif regiao == "Norte":
    frete = 30
    print(f"Frete de {regiao} é: {frete}")

else: 
    print("Não entregamos na sua região")

# Poderia diminuir linhas se no fim eu usasse if frete > 0: print frete, else print não entregamos
# Desse jeito, não teria que repitir os prints iguais



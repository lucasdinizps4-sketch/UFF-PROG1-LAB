# Faça um programa que receba o preço de um produto e seu código de origem e mostre sua procedência. A procedência obedece à tabela a seguir.

# código 1 = SUL
# código 2 = NORTE
# código 3 = LESTE
# código 4 = OESTE
# código 5 ou 6 = NORDESTE 
# código 7 ou 8 ou 9 = SUDESTE
# código 10 a 20 = CENTRO-OESTE
# código 21 a 30 = NORDESTE


preço_produto = float(input("Informe valor do preço do produto: "))
codigo = input("Informe o código do produto: ")

if codigo == "1": 
    procedencia = "SUL"

elif codigo == "2": 
        procedencia = "NORTE"

elif codigo == "3":
        procedencia = "LESTE"

elif codigo == "4":
        procedencia = "OESTE"
    
elif codigo == "5" or codigo == "6":
    procedencia = "NORDESTE"

elif codigo == "7" or codigo == "8" or codigo == "9":
    procedencia = "SUDESTE"

elif codigo >= "10" and codigo <= "20":
      procedencia = "CENTRO-OESTE"

elif codigo >= "21" and codigo <= "30": 
      procedencia = "NORDESTE"


print(f"Preço do produto é {preço_produto} e procedencia é de {procedencia}")




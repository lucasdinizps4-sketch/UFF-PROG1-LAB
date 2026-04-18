# Um supermercado deseja reajustar os preços de seus produtos usando o seguinte critério: o produto poderá ter seu preço aumentado ou diminuído. Para o preço ser alterado, o produto deve preencher pelo menos um dos -
# requisitos a seguir: 

# Venda média mensal, preço atual, % aumento, % diminuição 
# < 500, < 30, 10%, -
# >= 500 e < 1200, >= 30 e < 80, 15%, -
# >= 1200, >= 80, -, 20%

preco_atual = float(input("Informe valor atual do produto: "))
venda_m_m = int(input("Informe a venda média mensal: "))

if venda_m_m < 500 or preco_atual < 30:
    novo_preco = preco_atual + (preco_atual * 0.1)
    print(f"\nHouve um aumento no preço de {novo_preco - preco_atual}, agora o novo preço é de {novo_preco}")

elif (venda_m_m >= 500 and venda_m_m < 1200) or (preco_atual >= 30 and preco_atual < 80):
    novo_preco = preco_atual + (preco_atual * 0.15)
    print(f"\nHouve um aumento no preço de {novo_preco - preco_atual}, agora o novo preço é de {novo_preco}")

elif venda_m_m >= 1200 or preco_atual >= 80:
    novo_preco = preco_atual - (preco_atual * 0.2)
    print(f"\nHouve uma diminuição de preço de {novo_preco - preco_atual}, agora o novo preço é de {novo_preco}")

    # (PEDIR AJUDA DO LÉO)





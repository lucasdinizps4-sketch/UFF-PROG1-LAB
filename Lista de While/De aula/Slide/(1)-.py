# Um vendedor necessita de um programa que calcule o preço total devido por um cliente. O programa deve ler o código de um produto, a quantidade
# comprada, valor unitário e calcular o preço total de cada produto. Considere o último produto com o código igual a zero.

codigo = 1

while codigo != 0:
    if codigo == 0:
        break
    codigo = int(input("Informe código do produto: "))
    preco = int(input("Informe o preço: "))
    quantidade = int(input("Informe a quantidade desejada: "))

preco_final = preco * quantidade
print(f"Preço final = {preco_final}")
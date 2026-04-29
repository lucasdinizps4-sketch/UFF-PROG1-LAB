carrinho = []

while True:
    produto = input("Informe o produto que você quer adicionar (ou 'sair' para parar)")
    if produto == "sair":
        break
    if produto in carrinho:
        print("Produto já está no seu carrinho")
    else:
        carrinho.append(produto)

carrinho.sort()
print(f"Seu carrinho tem os seguintes itens: {carrinho}")
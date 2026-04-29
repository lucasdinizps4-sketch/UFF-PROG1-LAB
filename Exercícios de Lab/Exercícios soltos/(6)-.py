estoque = ["teclado", "mouse", "monitor", "fone"]

while True:
    item = input("Qual item deseja buscar? (Ou 'sair'): ")
    if item == "sair":
        break
    if item in estoque:
        posicao = estoque.index(item)
        print(f"Posição do item: {posicao}")
    else: 
        p1 = input("Item não encontrado, deseja adicionar ao carrinho? (s/n): ")
        if p1 == "s":
            estoque.append(item)

print(estoque)


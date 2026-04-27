# Peça ao usuário para inserir 5 números, que serão armazenados em uma lista. Em seguida, peça ao usuário um número inteiro N. O programa deve "girar" a lista para a direita
# N vezes. A cada giro, o último elemento se torna o primeiro.

lista_original = []

for i in range(5):
    num = int(input(f"Informe o valor {i+1}"))
    lista_original.append(num)

n = int(input("Informe um número inteiro: "))

for _ in range(n):
    ultimo = lista_original.pop()
    lista_original.insert(0, ultimo)
    print(lista_original)

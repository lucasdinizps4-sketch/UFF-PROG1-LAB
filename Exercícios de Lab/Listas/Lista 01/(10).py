soma = 0
contador = 0


while True:
    preco =float(input("Informe o preço do produto: (0 para sair) "))
    if preco == 0:
        break
    if preco < 0:
        print("Preço inválido, tente novamente.")
        continue
    soma = soma + preco
    contador = contador + 1

print(f"Total = {soma:.2f}")
print(f"Média = {soma/contador:.2f}")



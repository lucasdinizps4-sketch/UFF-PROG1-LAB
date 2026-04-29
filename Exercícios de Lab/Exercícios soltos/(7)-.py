dados = [10, 20, 10, 30, 40, 20, 50, 10]
limpos = []

for i in range(len(dados)):
    if dados[i] not in limpos:
        limpos.append(dados[i])

print(f"Lista final: {limpos}")


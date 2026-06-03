dados_alunos = [
    "Ana Silva: 8.5, 9.0, 7.5",
    "Bruno Costa: 6.0, 5.5, 7.0",
    "Carlos Dias: 9.5, 10.0, 9,0"
]

for i in range(len(dados_alunos)):
    dados_split = dados_alunos[i].split(": ")
    nome = dados_split[0]
    print(dados_split)
    nota = dados_split[1].split(",")
    soma = 0
    for j in range(len(nota)):
        soma += float(nota[j])
    media = soma / (len(nota))
    status = "Reprovado"
    if media >= 7.0:
        status = "Aprovado"

    print(f"Nome: {nome} | Média: {media:.2f} | Status: {status}")

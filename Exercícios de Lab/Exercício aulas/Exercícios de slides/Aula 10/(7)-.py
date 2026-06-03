# Crie um dicionário onde as chaves são nomes de alunos e os valores são listas contendo 3 notas. O programa deve percorrer o dicionário e exibir o nome de cada aluno junto com a
# sua média aritmética.

alunos = {
    "Lucas": [7,8,5],
    "Marcos": [3,6,5]
}

for chave,dados in alunos.items():
    soma = 0
    for i in dados:
        soma += i
    media = soma/(len(dados))
    print(f"Nome: {chave} \nMédia: {media:.2f}")






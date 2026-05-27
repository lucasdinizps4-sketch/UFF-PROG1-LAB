dados = open('Arquivos/dados_pessoas.txt', 'r', encoding = "utf-8")

for linha in dados:
    dados_pessoa = linha.split(";")
    print(f"Nome: {dados_pessoa[0]}")
    print(f"Idade: {dados_pessoa[1]}")
    print(f"Cidade: {dados_pessoa[2]}")

dados.close()
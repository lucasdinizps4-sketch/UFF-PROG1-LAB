dados_texto = open('Arquivos/dados.txt', 'r', encoding = "utf-8" )
linha = dados_texto.read() # Le todas linhas em uma string só, com \n ao final de toda linha
print(linha)
dados_texto.close()
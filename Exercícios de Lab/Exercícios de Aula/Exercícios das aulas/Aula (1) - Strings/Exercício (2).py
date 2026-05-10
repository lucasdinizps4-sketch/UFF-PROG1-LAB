# Dada uma URL completa, sua tarefa é extrair e exibir separadamente o protocolo, o domínio e o caminho (path).

url = "https://www.exemplo.com.br/produtos/eletronicos"

url2 = url.split("://") # Cria uma lista e usa "://" como separador, cortando a string em 2 substrings ["https", "www.exemplo.com.br/produtos/eletronicos"]. Não precisamos dizer em qual repetição do separador deveria parar, pois não existia outro "://": ("url.split("://",1)"")
prot = url2[0] # Busca o indice 0 na lista e armazena na variavel
url3 = url2[1].split("/",1) # Transforma url2[1] em uma lista, e põe separador "/" com 1 repetição, para parar separar na primeira / que ele ver: ["www.exemplo.com.br", "produtos/eletronicos"]
dom = url3[0] # Busca indice 0 na lista e armazena na variavel
cam = "/" + url3[1] # Concatena "/" com url3[1]: ("/" + produtos/eletronicos")


print(f"Protocolo: {prot}")
print(f"Domínio: {dom}")
print(f"Caminho: {cam}")
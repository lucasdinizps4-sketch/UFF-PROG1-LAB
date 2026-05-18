# Dada uma URL completa, sua tarefa é extrair e exibir separadamente o protocolo, o domínio e o caminho (path).

# Protocolo = https
# Dominio = www.exemplo.com.br
# Caminho = /produtos/eletronicos

url = "https://www.exemplo.com.br/produtos/eletronicos" 
lista_protocolo = url.split("://")
protocolo = lista_protocolo[0]
lista_dominio = lista_protocolo[1].split("/",1)
dominio = lista_dominio[0]
caminho = "/" + lista_dominio[1]

print(f"Protocolo = {protocolo} \nDominio = {dominio} \nCaminho = {caminho}")
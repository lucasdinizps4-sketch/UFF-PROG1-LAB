def media_exercicio(n1,n2):
    return (n1 * 1 + n2 * 2)/3

def media_f(media_exercicio,prova):
    return (media_exercicio * 0.2 + prova * 0.8)/10

def processar_arquivo(nomearquivo):
    arquivo = open(nomearquivo, "r", encoding = "utf-8")
    linha = arquivo.readline()
    while linha:
        nome,n1str,n2str,provastr = linha.strip().split(";")
        n1 = float(n1str)
        n2 = float(n2str)
        prova = float(provastr)
        media_ex = media_exercicio(n1,n2)
        media_final = media_f(media_ex,prova)
        print(f"Nome: {nome} | Exercício média: {media_ex:.3f} | Média final: {media_final:.3f}")
        linha = arquivo.readline()
    arquivo.close()

nome_arquivo = input("Informe nome do arquivo: ")
obter_arquivo = processar_arquivo(nome_arquivo)

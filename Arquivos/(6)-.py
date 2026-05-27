def mencao(nota):
    if nota >= 9 and nota <= 10:
        return "SS"
    elif nota >= 7 and nota <= 8.9:
        return "MS"
    elif nota >= 5 and nota <= 6.9:
        return "MM"
    elif nota >= 3 and nota <= 4.9:
        return "MI"
    elif nota >= 0.1 and nota <= 2.9:
        return "II"
    else:
        return "SR"
    


def processar_arquivo(nomearquivo):
    arquivo = open(nomearquivo, "r", encoding = "utf-8")
    linha = arquivo.readline()
    while linha:
        matricula,notastr = linha.strip().split(";")
        nota = float(notastr)
        mencaos = mencao(nota)
        print(f"Matricula: {matricula} \nMenção: {mencaos}")
        linha = arquivo.readline()
    arquivo.close
    
        
nome_arquivo = input("Informe nome do arquivo: ")
obter_arquivo = processar_arquivo(nome_arquivo)
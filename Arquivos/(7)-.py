def imposto(salario):
    if salario <= 1200: 
        return 0.0
    elif salario >= 1201 and salario <= 5000:
        return 0.1*salario
    elif salario >= 5001 and salario <= 10000:
        return 0.15*salario
    else:
        return 0.20*salario


def processar_arquivo(nomearquivo):
    arquivo = open(nomearquivo, "r", encoding = "utf-8")
    linha = arquivo.readline()

    while linha:
        nome,salariostr = linha.strip().split(";")
        salario = float(salariostr)
        imposto_ha_pagar = imposto(salario)
        print(f" Nome: {nome} | Salario: {salario} | Imposto: {imposto_ha_pagar}")
        linha = arquivo.readline()
    
    arquivo.close()

nome_arquivo = input("Informe o arquivo: ")
obter_arquivo = processar_arquivo(nome_arquivo)

        
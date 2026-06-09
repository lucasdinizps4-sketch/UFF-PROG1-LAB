def media_p(lista):
    soma = 0
    soma_p = 0
    for i in range(lista):
        nota = lista[i][0]
        peso = lista[i][1]
        soma += nota * peso
        soma_p += peso
    media = soma / soma_p
    return media



lista = [{"titulo": "O Hobbit", "genero": "Fantasia"}, {"titulo": "Duna", "genero": "Sci-Fi"}]


def filtrar_genero(lista,genero):
    lista_livro = []
    for livro in lista:
        if livro["genero"] == genero:
            lista_livro.append(livro["titulo"])
    return lista_livro

            
genero_escolhido = filtrar_genero(lista,"Fantasia")
print(genero_escolhido)
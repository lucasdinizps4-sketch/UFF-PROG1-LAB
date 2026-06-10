arquivo = open("poligonos.txt","r")
dados = arquivo.readlines()
arquivo.close

lista_tuplas = []
lista_areas = []

for i in range(len(dados)):
    dados_split = dados[i].strip().split()
    tipo = dados_split[0]
    base = dados_split[1]
    altura = dados_split[2]
    tuplas = (tipo,base,altura)
    lista_tuplas.append(tuplas)

    if tipo == "RET":
        area = base * altura
    else:
        area = (base*altura)/2

    lista_areas.append(area)

soma = 0
for i in range(len(lista_areas)):
    soma += lista_areas[i]

media = soma / len(lista_areas)
print(media)

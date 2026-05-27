# Para computar o vencedor de uma eleição deve ser feito um programa. 
# Há 3candidatos, e os votos dos eleitores foram codificados da seguinte forma:
# 1, 2 ou 3: votos para os respectivos candidatos
# 0: voto nulo

# Escrever o programa, que leia um arquivo que contém os votos codificados e forneça o
# vencedor da eleição (suponha que não pode haver empates), as quantidades de votos
# de cada candidatos, a quantidade de votos nulos e o número de eleitores que compareceram às urnas.


arquivo = open("Arquivos/votos.dat", "r", encoding = "utf-8")

votos_0 = 0
votos_1 = 0
votos_2 = 0
votos_3 = 0

for votos in arquivo:
    votos = votos.strip()
    if votos == "0":
        votos_0 += 1
    elif votos == "1":
        votos_1 += 1
    elif votos_2 == "2":
        votos_2 += 1
    else:
        votos_3 += 1
    
total_eleitores = votos_3+votos_2+votos_1+votos_0

if votos_1 > votos_2 and votos_1 > votos_3:
    print(f"O candidato eleito foi o 1, com {votos_1} votos")
elif votos_2 > votos_1 and votos_2 > votos_3:
    print(f"O candidato eleito foi o 2, com {votos_2} votos")
else:
    print(f"O candidato eleito foi o 3, com {votos_3} votos")

print(f"Total de eleitores foi {total_eleitores}")
print(f"Total de votos nulo foi {votos_0}")
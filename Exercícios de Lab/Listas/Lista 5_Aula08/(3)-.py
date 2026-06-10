# Escreva uma função na linguagem Python que receba uma lista de pares de comprimentos de catetos de triângulos retângulos e retorne uma lista com os
# comprimentos de cada respectiva hipotenusa. 

# Dica: h2 = a2 + b2, onde a e b são os catetos, h é a hipotenusa.


catetos = [(4,8),(6,8),(7,12)]

def hipotenusa(catetos):
    import math
    lista_hipotenusa = []
    for i in range(len(catetos)):
        a = catetos[i][0]
        b = catetos[i][1]
        h = math.sqrt(a**2 + b**2)
        lista_hipotenusa.append(h)
    return lista_hipotenusa

print(hipotenusa(catetos))

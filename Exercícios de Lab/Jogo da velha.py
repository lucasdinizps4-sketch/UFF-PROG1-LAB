


jogo = [
    [" ", " ", " "], 
    [" ", " ", " "], 
    [" ", " ", " "]   
]
casas_faltando = 0
jogador = "X"


while casas_faltando < 9:
    for i in range(len(jogo)):
        for j in range(len(jogo[i])):
            print(f"{jogo[i][j]}", end=" | ")
        print("\n----------------")
    if jogo[i][0] == jogo[i][1] and jogo[i][1] == jogo[i][2] and jogo[i][0] != " ":
        print(f"O jogador {jogo[i][0]} ganhou na linha [i]")
        break


    print(f"\nVez do jogador {jogador}\n")

    linha = int(input("Informe a linha: (0, 1 ou 2)"))
    casa = int(input("Informe a casa: (0, 1 ou 2)"))

    if jogo[linha][casa] == " ":
        jogo[linha][casa] = jogador
        casas_faltando += 1
        if jogador == "X":
            jogador = "O"
        else:
            jogador = "X"
    elif jogo[linha][casa] != " ":
        print("\n\nCasa está ocupada, tente dnv\n\n")
        continue


    




jogo = [
    [" ", " ", " "], 
    [" ", " ", " "], 
    [" ", " ", " "]   
]
casas_faltando = 0
jogador = "X"
venceu = False


while casas_faltando < 9:
    for i in range(len(jogo)):
        for j in range(len(jogo[i])):
            print(f"{jogo[i][j]}", end=" | ")
        print("\n------------")

    for i in range(len(jogo)):    

        if jogo[i][0] == jogo[i][1] and jogo[i][1] == jogo[i][2] and jogo[i][0] != " ":
            venceu = True
            print(f"\nO jogador {jogo[i][0]} ganhou na linha {[i]}\n")
        elif jogo[0][i] == jogo[1][i] and jogo[1][i] == jogo[2][i] and jogo[0][i] != " ":
            venceu = True
            print(f"O jogador {jogo[0][i]} ganhou na coluna {i}")
    if (jogo[0][0] == jogo[1][1] and jogo[1][1] == jogo[2][2] or jogo[0][2] == jogo[1][1] and jogo [1][1] == jogo[2][0]) and jogo[1][1] != " ":
        venceu = True
        print(f"O jogador {jogo[1][1]} venceu na diagonal")

    if venceu == True:
        break


    print(f"\nVez do jogador {jogador}\n")

    linha = int(input("\nInforme a linha: (0, 1 ou 2)"))
    casa = int(input("\nInforme a casa: (0, 1 ou 2)"))

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

print("\n\nDeu velha! Não houve vencedor")


    

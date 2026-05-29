


jogo = [
    [" ", " ", " "], 
    [" ", " ", " "], 
    [" ", " ", " "]   
]
casas_faltando = 0
jogador = "X" # Crio uma variavel jogador = x, para o x sempre começar a primeira jogada da partida. E após a jogada acontecer, faço uma troca de variveis dentro do loop
venceu = False # Crio essa variavel para dizer quando o programa termina, ou seja venceu = True


while casas_faltando < 9: # Criei um loop while com condição de casas no jogo, que no caso tem 9. Quando contador completar 9, o loop para
    for i in range(len(jogo)): # for para percorrer as linhas
        for j in range(len(jogo[i])): # for para percorrer as casas
            print(f"{jogo[i][j]}", end=" | ") # printa todas casas e divide com |
        print("\n------------") # printa separador de casas, fora do segundo for. Para sempre que ele terminar todas casas de uma linha, separar a outra linha e casa

    for i in range(len(jogo)): # For para as condições de vitória, pois antes estava quebrando o for de printar o jogo

        if jogo[i][0] == jogo[i][1] and jogo[i][1] == jogo[i][2] and jogo[i][0] != " ": # Condição de vitória na vertical, a linha sendo i vai sempre avanar até linha 2, depois de verificar todas casas. Ao final uma condição parar garantir que as primeiras não estejam vazias 
            venceu = True # Vencedor vira True
            print(f"\nO jogador {jogo[i][0]} ganhou na linha {[i]}\n") # Não usei {jogador}, pois daria errado. Ele sempre printaria o jogador seguinte, pois houve a troca de variaveis antes de testar as condições. Exemplo, caso X ganhasse, le imprimiria O pois houve uma troca
        elif jogo[0][i] == jogo[1][i] and jogo[1][i] == jogo[2][i] and jogo[0][i] != " ": # Inverti colocando i parar casa, desse modo consigo  
            venceu = True
            print(f"O jogador {jogo[0][i]} ganhou na coluna {i}") 
    if (jogo[0][0] == jogo[1][1] and jogo[1][1] == jogo[2][2] or jogo[0][2] == jogo[1][1] and jogo [1][1] == jogo[2][0]) and jogo[1][1] != " ": # Fiz de forma manual, comparando as extremidades e o ponto central
        venceu = True
        print(f"O jogador {jogo[1][1]} venceu na diagonal")

    if venceu == True: # Caso alguem vença ele quebra o programa
        break


    print(f"\nVez do jogador {jogador}") 

    linha = int(input("\nInforme a linha: (0, 1 ou 2): ")) # Crio as variaveis de coordenada e peço um valor para elas
    casa = int(input("\nInforme a casa: (0, 1 ou 2): "))

    if jogo[linha][casa] == " ": # Caso as coordenadas estejam vazias, adiciono valor de jogador nela
        jogo[linha][casa] = jogador # Adicionando valor de jogador na coordenada escolhida
        casas_faltando += 1 # Contador para sabermos quantas casas temos
        if jogador == "X": # Troca de variaveis, começa sempre com X. Caso seja X, vira O. 
            jogador = "O"
        else:
            jogador = "X" # Caso seja O vira X após a jogada
    elif jogo[linha][casa] != " ": # Caso as coordenadas não sejam vazias, printa uma mensagem de aviso e retorna para inicio
        print("\n\nCasa está ocupada, tente dnv\n\n")
        continue

if casas_faltando == 9:
    print("Deu velha! Não houve vencedor")
    for i in range(len(jogo)): # for para percorrer as linhas
        for j in range(len(jogo[i])): # for para percorrer as casas
            print(f"{jogo[i][j]}", end=" | ") # printa todas casas e divide com |
        print("\n------------")





    

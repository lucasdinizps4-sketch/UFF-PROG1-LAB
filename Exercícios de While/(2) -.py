# Crie um programa que leia a quantidade de kills feitas pelo jogador em cada round. Como você não sabe 
# quantos rounds o mapa vai ter (pode ser um rápido 7-0 ou um suado 8-7), o loop while deve continuar pedindo os valores até que você digite um número negativo (como -1), que será o sinal de parada da coleta.

kills = 0
rodada = 0
soma_kills = 0

while kills != -1 and rodada != 15:
    kills = int(input(f"\nInforme a quantidade de kills no round {rodada} (Digite -1 quando acabar): "))
    if kills == -1:
        break
    soma_kills += kills
    rodada += 1

print(f"\nVocê teve {soma_kills} em {rodada} rodadas \nMédia de kills = {soma_kills/rodada:.1f}")


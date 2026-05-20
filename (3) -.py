# O Desafio:
# O programa deve ler repetidamente uma string indicando quem marcou o gol na rodada, aceitando as letras "F" (gol do Fluminense) ou "R" (gol do Real Madrid).
# O loop while deve continuar rodando ininterruptamente até que uma destas duas condições de fim de jogo seja atingida:

# Alguém consiga abrir 3 gols de vantagem sobre o outro.

# O total de gols marcados (somando os dois lados) chegue ao limite de 10 cobranças convertidas.

# Ao encerrar o loop, imprima o placar final e a mensagem de quem foi o vencedor (ou se o jogo terminou em um empate técnico de 5 a 5).


gol_flu = 0
gol_real = 0
total_gols = 0
vantagem_flu = 0
vantagem_real = 0

while vantagem_flu < 3 and vantagem_real < 3 and total_gols < 10:
    time = input("Quem fez o gol? (F/R)").upper()
    if time == "F":
        gol_flu += 1
    else: 
        gol_real += 1
    total_gols += 1
    vantagem_flu = gol_flu - gol_real
    vantagem_real = gol_real - gol_flu
    print(f"\nPlacar: Flu:{gol_flu} x Real:{gol_real}\n")
    
if gol_flu > gol_real:
    print(f"Fluminense ganhou com placar de: {gol_flu} x {gol_real}")
elif gol_real > gol_flu:
    print(f"Real Madrid ganhou com placar de: {gol_real} x {gol_flu}")
else:
    print(f"Partida terminou em empate! Placar de {gol_flu} x {gol_real}")



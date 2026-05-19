jogo = [
["x", "o", "x"],
["o", " ", "x"],
[" ", "x", "o"]
]

for i in range(len(jogo)):
    for j in range(len(jogo[i])):
        print(f"{jogo[i][j]}", end=" | ")
    print('\n--------------')


# Escreva um programa em python, para imprimir quantos caracteres existem antes do primeiro espaço em branco

frase = "Lucas Diniz"
i = 0
count = 0

while frase[i] != " ":
    count += 1
    i += 1
    print(count)
print("Espaço em branco!")


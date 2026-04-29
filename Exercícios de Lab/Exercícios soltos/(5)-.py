notas = []
soma = 0 
aprovados = []

while True:
    nota = float(input("Informe sua nota"))
    if nota == -1:
        break
    else:
        notas.append(nota)


for i in range(len(notas)):
    soma = soma + notas[i]
    if notas[i] >7:
        aprovados.append(notas[i])

media = soma / len(notas)

print(f"Média = {media:.1f}")
print(f"Aprovados: {aprovados}")


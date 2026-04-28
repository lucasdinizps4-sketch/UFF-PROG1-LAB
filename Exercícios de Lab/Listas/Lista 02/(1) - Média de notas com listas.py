# Escreva um programa que funcione como uma calculadora de média para um aluno. O
# programa deve pedir para o usuário digitar as notas uma a uma. O usuário poderá inserir
# quantas notas desejar. Para encerrar a inserção de notas, o usuário deve digitar -1. Após a
# inserção ser encerrada, o programa deve calcular e exibir a média das notas inseridas.

lista_notas = []
nota = 0
soma = 0

while nota != -1:
    nota = int(input("informe sua nota: "))
    if nota == -1:
        break
    lista_notas.append(nota)
    soma = soma + nota

media = soma / len(lista_notas)

print(media)
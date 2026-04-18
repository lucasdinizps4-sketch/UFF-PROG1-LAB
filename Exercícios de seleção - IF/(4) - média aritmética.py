# Faça um programa que receba três notas de um aluno, calcule e mostre a média aritmética e a mensagem constante na tabela a seguir. Aos alunos que ficaram para exame, calcule e mostre a nota que deverão tirar para serem aprovados, considerando que a média exigida é 6,0.

# >= 0 and < 3 ---> Reprovado
# >= 3 and < 7 ---> Exame
# >= 7 and <= 10 ---> Aprovado

n1 = float(input("Informe sua nota da primeira prova: "))
n2 = float(input("Informe sua nota da segunda prova: "))
n3 = float(input("Informe sua nota da terceira prova: "))

media = (n1+n2+n3) / 3

if media >= 0 and media < 3:
    status = "Reprovado"

elif media >= 3 and media < 7:
    status = "Exame"

elif media >= 7 and media <= 10:
    status = "Aprovado"

print(f"Sua méddia foi {media:.2f}, com status de {status}")


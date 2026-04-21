# Escreva um programa que leia 5 pares de 2 valores, o primeiro representando a matrícula de um aluno e o segundo representando a sua -
# altura em centímetros. Encontrar o aluno mais alto e o mais baixo e escrever suas matrículas, suas alturas e uma mensagem dizendo se é o mais alto ou -
# o mais baixo. 

matricula = input("Informe a matrícula: ")
altura_cm = float(input("Informe sua altura em cm: "))

maior_altura = altura_cm
menor_altura = maior_altura
matricula_maior = matricula
matricula_menor = matricula

for i in range(1,5,1):
    altura_cm = int(input("Informe sua altura em cm: "))
    matricula = input("Informe sua matrícula")
    if altura_cm > maior_altura:
        maior_altura = altura_cm
        matricula_maior = matricula
    elif altura_cm < menor_altura:
        menor_altura = altura_cm
        matricula_menor = matricula
    
print(f"\nAluno mais alto: {maior_altura} \nMatrícula: {matricula_maior} \n\nAluno mais baixo: {menor_altura} \nMatrícula: {matricula_menor}")
# Escreva um programa que leia um arquivo (pessoas.dat) contendo o nome, email, sexo, idade de várias pessoas e imprima os dados lidos
# das pessoas de sexo feminino,total de homens e o total de mulheres.

dados = open('Arquivos/pessoas.dat', "r", encoding = 'utf-8')

total_homens = 0
total_mulheres = 0
total_idade_f = 0
total_idade_m = 0

for linha in dados:
    nome,email,sexo,idade = linha.split(";")
    if sexo == "F":
        print(nome,email,sexo,idade, sep="\t")
        total_mulheres += 1
        total_idade_f += int(idade)
    else: 
        total_homens += 1
        total_idade_m += int(idade)

media_idadefem = total_idade_f / total_mulheres
media_idadem = total_idade_m / total_homens
    

print(f"Total de homens: {total_homens} \nTotal de mulheres: {total_mulheres} \nMédia de idade homens: {media_idadem} \nMédia de idade mulheres: {media_idadefem}")
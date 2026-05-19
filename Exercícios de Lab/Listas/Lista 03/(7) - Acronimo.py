# Faça um programa que peça ao usuário para digitar um nome ou expressão (ex: "HyperText Markup Language"). O programa deve gerar e exibir um acrônimo pegando a
# primeira letra de cada palavra em maiúsculas (ex: "HTML"). 

nome = input("Informe uma frase: ").title()
acronimo = ""
lista_nome = nome.split()

for i in lista_nome:
    acronimo += i[0]
print(acronimo)

# Escreva um programa para calcular o comprimento (sem utilizar len) de uma
# string.

s1 = input("Informe uma frase: ")
contador = 0
vazio = 0

for i in s1:
    if i == " ":
        vazio += 1
    elif i != " ":
         contador += 1
       

print(f"{s1} tem {contador} letras e {vazio} espaços vazios")
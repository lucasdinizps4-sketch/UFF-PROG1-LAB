# Escreva um programa contar todas as letras, dígitos e símbolos especiais de uma determinada string.

contador_letras = 0
contador_digitos = 0
contador_simbolos = 0 

s1 = input(f"Informe uma frase, utilizando letras, digitos e simbolos: ")

for i in s1:
    if i == " ":
        print("Carácter vazio")
    else:
        if i.isnumeric():
            contador_digitos += 1
        elif i.isalpha():
            contador_letras += 1
        else:
            contador_simbolos += 1
print(f"Letras = {contador_letras} \nDígitos = {contador_digitos} \nSímbolos = {contador_simbolos}")




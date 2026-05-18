# Peça ao usuário para digitar uma frase. Seu programa deve contar e exibir quantas palavras existem nessa frase.

frase = input("Informe uma frase: ")
lista_frase = frase.split(" ") 
print(lista_frase)
print(f"{frase} tem {len(lista_frase)} palavras")
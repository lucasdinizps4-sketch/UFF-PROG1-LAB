# Criar um gerador de hashtags a partir de uma frase. A hashtag deve começar com #, ter todas as palavras juntas, e cada palavra deve iniciar
# com letra maiúscula.

frase = input("Informe uma frase")
frase1 = frase.title() # Deixa toda letra que começa uma palavra, maiúscula
frase2 = frase1.split() # Cria uma lista com substrings ["Lucas" "Diniz"]
frase3 = "".join(frase2) #Transforma lista em string ("".join retorna string sem espaços, mas com " " retorna com espaços)
frase_final = "#" + frase3 # Concatena "#" com string

print(frase_final)
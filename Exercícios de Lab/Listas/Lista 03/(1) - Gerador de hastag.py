# Criar um gerador de hashtags a partir de uma frase. A hashtag deve começar com #, ter todas as palavras juntas, e cada palavra deve iniciar
# com letra maiúscula.

frase_original = "Python é muito legal"
letrasI_maisculas = frase_original.title()
lista = letrasI_maisculas.split()
hastag = "#" + "".join(lista)
print(hastag)
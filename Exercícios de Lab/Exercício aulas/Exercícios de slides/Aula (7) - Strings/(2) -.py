# FAÇA UM PROGRAMA QUE VERIFIQUE SE A PALAVRA É UM PALINDROMO

frase = input().lower()

if frase == frase[::-1]:
    print("Palíndromo")
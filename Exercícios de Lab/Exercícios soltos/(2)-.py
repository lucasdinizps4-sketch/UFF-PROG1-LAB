bons_palindromos =[]

while True:
    palavra = input("Digite uma palavra (ou 'sair')")
    if palavra == "sair":
        break
    else:
        palavra_invertida = ""
        for i in range(len(palavra)-1,-1,-1):
            palavra_invertida = palavra_invertida + palavra[i]
        if palavra_invertida == palavra:
            bons_palindromos.append(palavra_invertida)
            print(f"A palavra {palavra} é um palíndromo")
        else:
            print(f"A palavra {palavra} não é um palíndromo")

print(f"Os palíndromos são: {bons_palindromos}")
mensagem = input()
chave = int(input())
modo = input()
alfabeto = "ABCD..."
nova_frase = ""

if modo == "criptografar":

    for i in range(len(mensagem)):
        caractere = mensagem[i]

        if caractere in alfabeto:
            indice_atual = alfabeto.find(caractere)
            novo_indice += (indice_atual + chave) % 26
            nova_frase += alfabeto[novo_indice]
        else:
            nova_frase += mensagem[i]

print(f"Mensagem criptgrafada: {nova_frase}")
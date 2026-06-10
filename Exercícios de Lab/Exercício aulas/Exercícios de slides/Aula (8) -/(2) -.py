mensagem = input()
chave = int(input())
modo = input()
alfabeto = "abcdefghijklmnopqrstuvwxyz"
nova_frase = ""

if modo == "descriptografar":
    chave = chave *(-1)

for i in range(len(mensagem)):
    caractere = mensagem[i].lower()

    if caractere in alfabeto:
        indice_atual = alfabeto.find(caractere)
        novo_indice = (indice_atual + chave) % 26
        nova_frase += alfabeto[novo_indice]
    else:
        nova_frase += mensagem[i]

if modo == "descriptografar":
    print(f"Mensagem criptgrafada: {nova_frase}")

else:
    print(f"Mensagem descriptgrafada: {nova_frase}")


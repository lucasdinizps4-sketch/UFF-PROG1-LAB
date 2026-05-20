# Escreva um programa para ler uma string e inverter 

frase = "Lucas Diniz"
frase_invertida = ""

for i in range(len(frase)-1,-1,-1): # Len(frase)-1 pois sem a subtração ele retorna n de letras
    frase_invertida += frase[i]

print(frase_invertida)

# PODERIAOS USAR MÉTODO DE LISTA, MAS NÃO FOI PASSADO

frase = "Lucas Diniz"
frase_invertida = frase[::-1]
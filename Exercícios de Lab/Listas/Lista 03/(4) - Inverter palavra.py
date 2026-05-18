# Escreva um programa que peça uma palavra ao usuário e a imprima de trás para frente.

palavra = input("Informe uma palavra, para inverter: ")
palavra_invertida = palavra[::-1]
print(palavra_invertida)

# USANDO FOR 

palavra = input("Informe uma palavra, para inverter: ").lower()
palavra_invertida = ""

for i in range(len(palavra)-1,-1,-1):
    palavra_invertida += palavra[i]

print(palavra_invertida)
# Faça um programa que verifique se uma palavra digitada pelo usuário é um palíndromo.
# Um palíndromo é uma palavra que se lê da mesma forma de trás para frente.

palavra = input("Informe uma palavra: ")

if palavra == palavra[::-1]:
    print("Palíndromo")
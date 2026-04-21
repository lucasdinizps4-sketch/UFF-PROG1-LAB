# Escreva um programa que leia seis conjuntos de três valores, representando o:
#  comprimento, largura e altura de caixas retangulares e calcule o volume de cada uma, cuja fórmula é: VOLUME = COMPRIMENTO * LARGURA * ALTURA. 

caixa = 0

for i in range(6):
    largura = float(input("\nInforme a largura: "))
    altura = float(input("Informe a altura: "))
    comprimento = float(input("Informe o comprimento: "))
    volume = comprimento * largura * altura
    caixa = caixa + 1
    print(f"\nVolume da caixa {caixa} é: {volume}")
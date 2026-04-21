# Escreva um programa que leia quinze conjuntos de dois valores PRESTAÇÃO e TAXA, representando o valor de uma prestação e a taxa de juros cobrada pelo atraso. 
# Calcule cada prestação atrasada pela fórmula: ATRASO = PRESTAÇÃO + (PRESTAÇÃO* TAXA /100)

for i in range(15):
    prestacao = int(input("\nInforme valor da prestação: "))
    taxa = float(input("Informe taxa: "))
    atraso = prestacao + (prestacao * taxa/100)
    n_prestacao = i + 1
    print(f"\n Prestação ({n_prestacao}), Valor: {prestacao}, Atraso: {atraso}")


# Construa um programa que recebe a estatura de usuário em metros e converte para centímetros. 
# Exemplo de saída: “Sua altura em centímetros é x.xx.”

m = float(input("Informe sua altura em metros: "))
cm = 100*m 
print(f"Sua altura em centímetros é: {cm:.0f}")

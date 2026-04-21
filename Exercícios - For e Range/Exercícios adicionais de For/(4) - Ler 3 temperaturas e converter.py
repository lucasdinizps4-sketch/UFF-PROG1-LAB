# Escreva um programa que leia três temperaturas em grau Fahrenheit e converta cada uma para graus Celsius, cuja fórmula de conversão é: (graus Fahrenheit – 32) * (5/9).

for i in range(3):
    temperatura_fh = float(input("Informe o valor em Fahrenheit: "))
    conversao = (temperatura_fh - 32) * (5/9)
    temperatura_c = conversao
    print(f"\nTemperatura em Fahrenheit: {temperatura_fh} \nConversão para Graus: {temperatura_c:.1f} ")
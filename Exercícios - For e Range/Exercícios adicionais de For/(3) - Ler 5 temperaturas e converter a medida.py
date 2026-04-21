# Escreva um programa que leia cinco temperaturas em graus Celsius e converta cada uma para grau Fahrenheit, cuja fórmula de conversão é: ( 9 * graus Celsius + 160 ) /5.

for i in range(5):
    temperatura_c = float(input("\nInforme temperatura em graus: "))
    temperatura_fh = (temperatura_c * 9 + 160) / 5
    print(f"\nTemperatura em graus: {temperatura_c} \nConversão para Fahrenheit: {temperatura_fh}")
    

# Para A e B inteiros e maiores que zero, fazer um programa para o cálculo de A elevado à potência de B usando multiplicações sucessivas.
a = int(input("Informe valor de A: "))
b = int(input("Informe valor de B: "))

if a == 0 or b == 0: 
    print("A e B não podem ser 0")
else:
    resultado = 1
    for i in range(b):
        resultado = resultado * a
        
    print(f"Resultado de {a} elevado a {b} = {resultado}")
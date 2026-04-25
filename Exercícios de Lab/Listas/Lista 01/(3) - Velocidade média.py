# Construa um programa que receba do usuário a variação do deslocamento de um objeto (em metros) e a variação do tempo percorrido (em segundo). Ao fim, o programa deve
# calcular a velocidade média, em m/s, do objeto.

VD = float(input("Informe a variação do deslocamento em metros: "))
VT = float(input("Informe a variação do tempo percorrido em segundos: "))

if VD == 0 or VT == 0:
    print("Dados invalidos")
else:
    VM = VD/VT  
    print(f"Velocidade média = {VM}m/s")
# Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10 metro e cresce 3 centímetros por ano. Construa um programa que calcule e
# imprima quantos anos serão necessários para que Zé seja maior que Chico. 

chico_h = 1.50
ze_h = 1.10
ano = 0 

while chico_h > ze_h:
    chico_h += 0.2
    ze_h += 0.3
    ano += 1

print(f"Zé irá ultrapassar Chico em {ano} anos")
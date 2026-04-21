# Escrever um programa que leia 5 valores, um de cada vez, e conta quantos deles estão em cada um dos intervalos: [0, 25], (25, 50], (50, ∞).

nde025 = 0
nde2550 = 0 
nmaiorque50 = 0

for i in range(5):
    N = int(input())
    if N >= 0 and N <= 25:
        nde025 = nde025 + 1
    elif N > 25 and N <= 50:
        nde2550 = nde2550 + 1
    elif N > 50:
        nmaiorque50 = nmaiorque50 + 1

    print(f"Valores [0,25]: {nde025} ")
    print(f"Valores [25,50]: {nde2550} ")
    print(f"Valores [50, ∞]: {nmaiorque50} ")
    

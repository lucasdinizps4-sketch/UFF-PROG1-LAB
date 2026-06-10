# A Conjectura de Collatz é um problema matemático que trata de sequências de números. A sequência segue uma regra, definida da seguinte maneira:

# Partindo de um número inteiro positivo x, o próximo número da sequência é calculado por:
# ● se x for par, próximo = x / 2
# ● se x for ímpar, próximo = 3x + 1

# Em uma rodada seguinte, o número calculado pelas expressões acima deve ser usado
# como x. O processo continua até que o próximo número da sequência seja 1.

N = int(input())

while N != 1:
    if N % 2 == 0: 
        N = N/2
    else:
        N = 3 * N + 1
    print(N)
print("FIM")

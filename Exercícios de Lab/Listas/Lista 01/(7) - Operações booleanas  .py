# Crie um programa que peça para o usuário digitar dois números. O programa deve então imprimir o resultado Booleano (True ou False) para cada uma das seguintes afirmações:
# O primeiro número é igual ao segundo.
# O primeiro número é diferente do segundo.
# O primeiro número é maior que o segundo.
# O primeiro número é menor ou igual ao segundo.

n1 = int(input("Informe N1: "))
n2 = int(input("Informe N2: "))

print(f"{n1} é igual a {n2}: {n1==n2}")
print(f"{n1} é diferente de {n2}: {n1!=n2}")
print(f"{n1} é maior que {n2}: {n1>n2}")
print(f"{n1} é menor ou igual que {n2}: {n1<=n2}")
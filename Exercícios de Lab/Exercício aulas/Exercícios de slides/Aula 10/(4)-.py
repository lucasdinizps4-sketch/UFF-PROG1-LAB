texto = input("Informe um texto curto: ")
lista = texto.split()
conjunto = set(lista)
print(f"{len(conjunto)}")

# Outro jeito abaixo 

texto = input()
print(len(set(texto.split())))
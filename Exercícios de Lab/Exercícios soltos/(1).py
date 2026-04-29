# Faça uma lista de convidados com 4 pessoas, depois faça um programa que pede N convidados, quantos ele quiser adicionar.
# Quando o usuário estiver satisfeito, pergunte se ele quer remover alguem, com limite de 3 pessoas

lista_original = []

for i in range(4): 
    lista_original.append(input(f"Informe o convidado número {i+1}: "))
print(f"\nSua lista inicial é {lista_original}")

while True:
    p1 = input("\nVoce quer adicionar alguém na lista original? (s/n): ")
    if p1 == "n":
        print(f"\nOk, sua lista final é {lista_original}!")
        break
    if p1 == "s":
        lista_original.append(input(f"Informe o convidado que você quer adicionar: "))

p2 = input("\nPerfeito, você quer remover alguém? (s/n): ")

print("Caso você responda sim, você só podera remover 3 convidados!")

if p2 == "s":
    for i in range(3):
        escolha = input("Quem você quer remover: ")
        if escolha in lista_original:
            lista_original.remove(escolha)
            print(f"Faltam {2-i} convidados ")
        else: 
            print(f"Erro, {escolha} não está na sua lista")
else:
    print(f"Ok, sua lista definitiva é {lista_original}")

print(f"\nSua lista definitiva é {lista_original}")


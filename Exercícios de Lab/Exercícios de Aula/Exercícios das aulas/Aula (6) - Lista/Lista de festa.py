lista_original = ["Talita", "Raquel", "Duda"]
print(f"Lista da sua festa: {lista_original}")

p1 = input("\nVocê quer adicionar alguém na festa? (s/n): ")

if p1 == "s": 
    lista_original.append(input("Quem você quer adicionar?: "))

print("\nUm dos candidatos cancelou presença na festa")

lista_original.remove(input("Escolha um convidado para remover da festa: "))

lista_original.sort()

print(f"\nSua nova lista da festa é: {lista_original}")






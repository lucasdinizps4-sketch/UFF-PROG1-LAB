from funcoes_lista import add_lista
from funcoes_lista import pos_menor
from funcoes_lista import obtermenor_por_pos
from funcoes_lista import permutar
from funcoes_lista import ordenar_lista

minha_lista = []
quantidade = int(input("Quantos números você quer na lista?: "))
add_lista(minha_lista,quantidade)
print(minha_lista)

permutacao = input(f"Você quer permutar dois elementos da lista? (S/N): ").upper()
if permutacao == "S":
    p1 = int(input("Qual posição você quer permutar?: "))
    p2 = int(input("Com qual posição? "))
    permutar(minha_lista,p1,p2)
    print(f"Nova lista com permutação de posição {p1} com posição {p2}: {minha_lista}")

apartir_de = int(input("De qual posição você quer começar?: "))
achar_menor = obtermenor_por_pos(minha_lista,apartir_de)
print(f"Posição do menor número: {achar_menor}")
ordenar_lista(minha_lista)
print(f"Lista ordenada {minha_lista}")






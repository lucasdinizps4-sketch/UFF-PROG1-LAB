from funcoes_lista import ordenar_lista
from funcoes_lista import add_lista

def p_binaria(lista,valor):
    inicio = 0
    fim = len(lista)-1
    while inicio <= fim:
        meio = int((inicio+fim)/2)
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1


minha_lista = []
lista_qntd = int(input("Informe quantos valores você quer na lista: "))
add_lista(minha_lista,lista_qntd)
ordenar_lista(minha_lista)

n = int(input("Qual valor você quer achar na lista?: "))
posicao_n = p_binaria(minha_lista,n)
if posicao_n == -1:
    print(f"{n} não está na lista!")
else:
    print(f"Posição de {n} na lista é {posicao_n}!")


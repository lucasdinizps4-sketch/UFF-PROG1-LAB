def add_lista(lista,qnt):
    for _ in range(qnt):
        n = int(input("Informe valor de N: "))
        lista.append(n)

def pos_menor(lista):
    menor = lista[0]
    p_menor = 0
    for i in range(1,len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            p_menor = i
    return p_menor

def obtermenor_por_pos(lista,posinicial):
    menor = lista[posinicial]
    p_menor = posinicial
    for i in range(posinicial+1,len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            p_menor = i
    return p_menor

def permutar(lista,p1,p2):
    aux = lista[p1]
    lista[p1] = lista[p2]
    lista[p2] = aux

def ordenar_lista(lista):
    for posinicial in range(len(lista)-1):
        posmenor = obtermenor_por_pos(lista,posinicial)
        if posmenor != posinicial:
            permutar(lista,posmenor,posinicial)





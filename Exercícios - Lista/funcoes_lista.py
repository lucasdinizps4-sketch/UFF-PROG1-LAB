
# Escreva uma função para ler a quantidade valores inteiros que o usuário quiser e add em uma lista 
def add_lista(lista,qnt):
    for _ in range(qnt):
        n = int(input("Informe valor de N: "))
        lista.append(n)


# Escreva uma função para devolver a posição do menor valor inteiro em uma lista
def pos_menor(lista):
    menor = lista[0]
    p_menor = 0
    for i in range(1,len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            p_menor = i
    return p_menor


# Escreva uma função para descobrir o menor valor inteiro em uma lista de apartir de uma posição
def obtermenor_por_pos(lista,posinicial):
    menor = lista[posinicial]
    p_menor = posinicial
    for i in range(posinicial+1,len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            p_menor = i
    return p_menor


# Escreva uma função para permutar 2 valores na lista de acordo com os indices passados
def permutar(lista,p1,p2):
    aux = lista[p1]
    lista[p1] = lista[p2]
    lista[p2] = aux


# Escreva uma função para ordenar uma lista
def ordenar_lista(lista):
    for posinicial in range(len(lista)-1):
        posmenor = obtermenor_por_pos(lista,posinicial)
        if posmenor != posinicial:
            permutar(lista,posmenor,posinicial)





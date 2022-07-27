from xml.dom.minidom import Element


def menor_elemento_lista(lista):
    for elemento in lista:
        if type(elemento) not in [int, float]:
            raise TypeError("O valor do elemento deve ser um número real ou inteiro")
    for i in range(len(lista)):
        if i == 0:
            menor_elemento = lista[i]
            indice = i
        elif lista[i] < menor_elemento:
            menor_elemento = lista[i]
            indice = i
            return menor_elemento, indice


def reposicao_q1(lista):
    contador = 0
    for elemento in lista:
        if elemento[1] < 5:
            contador = contador + 1
    return contador


def venda_q2(lista):
    def percentual_arredondado(valor, total):
        return round(valor / total, 4)

    total_vendidos = 0
    venda_id1 = 0
    venda_id2 = 0
    venda_id3 = 0

    for elemento in lista:
        total_vendidos = total_vendidos + elemento[2]

    for elemento in lista:
        if elemento[1] == 1:
            venda_id1 = venda_id1 + elemento[2]

    for elemento in lista:
        if elemento[1] == 2:
            venda_id2 = venda_id2 + elemento[2]

    for elemento in lista:
        if elemento[1] == 3:
            venda_id3 = venda_id3 + elemento[2]

    print(total_vendidos, venda_id1, venda_id2, venda_id3)
    return [
        (1, percentual_arredondado(venda_id1, total_vendidos)),
        (2, percentual_arredondado(venda_id2, total_vendidos)),
        (3, percentual_arredondado(venda_id3, total_vendidos)),
    ]


def sum_q3(lista):
    contador = 0
    for elemento in lista:
        contador = contador + elemento[1]
    return round(contador, 2)

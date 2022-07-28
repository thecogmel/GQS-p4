def alunos_matriculados(lista, id_turma):
    contador = 0
    for elemento in lista:
        if elemento[0] == id_turma:
            contador = contador + 1
    return contador


def turma_matriculada(lista, id_turma):
    contador = 0
    for elemento in lista:
        if elemento[1] == id_turma:
            contador = contador + 1
    return contador


def maior_turma(lista):
    contador_primeira_turma = 0
    contador_segunda_turma = 0
    for elemento in lista:
        if elemento[0] == 1:
            contador_primeira_turma = contador_primeira_turma + 1

    for elemento in lista:
        if elemento[0] == 2:
            contador_segunda_turma = contador_segunda_turma + 1

    if contador_primeira_turma > contador_segunda_turma:
        return 1
    else:
        return 2

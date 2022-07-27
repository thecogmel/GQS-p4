from conexaoDB import *


def ler_todos_alunos(bd):
    return ler_bd(bd, "SELECT * FROM Aluno")


""" def ler_usuario_nome(bd, nome):
    query = "SELECT * FROM Usuario WHERE nome = ?"
    return ler_bd(bd, query, (nome,)) """


# PARAMETRO DE QUERY INCOMPLETA


""" def ler_produtos(bd):
    return ler_bd(bd, "SELECT * FROM Produto ORDER BY CATEGORIA, NOME") """

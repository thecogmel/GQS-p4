from conexaoDB import *


def ler_turma_Carla(bd):
    query = "SELECT Matricula.id_turma FROM Matricula INNER JOIN Aluno ON Matricula.id_aluno = Aluno.id WHERE Aluno.id = 1"
    return ler_bd(bd, query)


def ler_todos_alunos(bd):
    return ler_bd(bd, "SELECT * FROM Aluno")


def ler_turmas_geografia(bd):
    return ler_bd(bd, "SELECT nome, id_disciplina FROM Turma WHERE id_disciplina = 1")

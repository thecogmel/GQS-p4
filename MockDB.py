from unittest import TestCase
import sys

sys.path.insert(0, "..")
from conexaoDB import *

BD = "TestBD.db"


class MockBD(TestCase):
    @classmethod
    def setUpClass(cls):
        con = conectar(BD)
        cursor = con.cursor()
        query_criar_tabela_aluno = (
            """CREATE TABLE Aluno (id int NOT NULL PRIMARY KEY, nome TEXT NOT NULL)"""
        )
        query_criar_tabela_disciplina = """CREATE TABLE Disciplina (id int NOT NULL PRIMARY KEY, nome TEXT NOT NULL)"""
        query_criar_tabela_turma = """CREATE TABLE Turma (id int NOT NULL PRIMARY KEY, nome TEXT NOT NULL, turno text NOT NULL, id_disciplina INT , FOREIGN KEY (id_disciplina) REFERENCES Disciplina(id))"""
        query_criar_tabela_matricula = """CREATE TABLE Matricula (id int NOT NULL PRIMARY KEY,  id_aluno INT, id_turma INT ,FOREIGN KEY (id_aluno) REFERENCES Aluno(id), FOREIGN KEY (id_turma) REFERENCES Turma(id))"""
        try:
            cursor.execute(query_criar_tabela_aluno)
            cursor.execute(query_criar_tabela_disciplina)
            cursor.execute(query_criar_tabela_turma)
            cursor.execute(query_criar_tabela_matricula)

            con.commit()
        except sqlite3.Error as error:
            print("Erro na criação das tabelas:", error)
        else:
            print("Criação das tabelas: OK")

        query_inserir_aluno = """INSERT INTO Aluno (id, nome) VALUES
                                    (1, 'Carla F'),
                                    (2, 'Danilo'),
                                    (3, 'Daniel'),
                                    (4, 'Alice'),
                                    (5, 'Alice'),
                                    (6, 'Alice'),
                                    (7, 'Alice'),
                                    (8, 'Alice')"""
        query_inserir_disciplina = """INSERT INTO Disciplina (id,nome) VALUES
                                    (1, 'geografia'),
                                    (2,'mamatica' ),
                                    (3, 'quimica'),
                                    (4, 'fisica')"""
        query_inserir_turma = """INSERT INTO Turma (id,nome,turno,id_disciplina) VALUES
                                    (1, 'Tads01','manha',1),
                                    (2, 'Tads02','tarde',1),
                                    (3, 'Tads03','manha',2),
                                    (4, 'Tads04','noite',3)"""
        query_inserir_matricula = """INSERT INTO Matricula (id,id_aluno,id_turma) VALUES
                                    (1,1,1),
                                    (2,1,3),
                                    (3,2,4),
                                    (4,3,3)"""
        try:
            cursor.execute(query_inserir_aluno)
            cursor.execute(query_inserir_disciplina)
            cursor.execute(query_inserir_turma)
            cursor.execute(query_inserir_matricula)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na inserção de dados:", error)
        else:
            print("Inserção dos dados: OK")
            cursor.close()
            desconectar(con)
        testconfig = {"bd": BD}
        cls.mock_db_config = testconfig

    @classmethod
    def tearDownClass(cls):
        print("TearDown")
        con = conectar(BD)
        cursor = con.cursor()
        try:
            cursor.execute("DROP TABLE Aluno")
            cursor.execute("DROP TABLE Disciplina")
            cursor.execute("DROP TABLE Turma")
            cursor.execute("DROP TABLE Matricula")
            con.commit()
            cursor.close()
            print("Removeu os dados das tabelas.")
        except sqlite3.Error as error:
            print("Banco de dados não existe. Erro na remoção do BD.", error)
        finally:
            desconectar(con)

from MockDB import MockBD
import sys

sys.path.insert(0, "..")
from conexaoDB import *
from queries import *


class TestDB(MockBD):
    def test_all_class_of_Carla(self):
        retorno_esperado = [(1,), (3,)]
        self.assertEqual(
            ler_turma_Carla(self.mock_db_config.get("bd")), retorno_esperado
        )

    def test_select_all_02(self):
        retorno_esperado = [
            (1, "Carla F"),
            (2, "Danilo"),
            (3, "Daniel"),
            (4, "Alice"),
            (5, "Alice"),
            (6, "Alice"),
            (7, "Alice"),
            (8, "Alice"),
        ]
        self.assertEqual(
            ler_todos_alunos(self.mock_db_config.get("bd")), retorno_esperado
        )

    def test_geography_class_03(self):
        retorno_esperado = [("Tads01", 1), ("Tads02", 1)]
        self.assertEqual(
            ler_turmas_geografia(self.mock_db_config.get("bd")), retorno_esperado
        )

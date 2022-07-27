from MockDB import MockBD
import sys

sys.path.insert(0, "..")
from conexaoDB import *
from queries import *


class TestDB(MockBD):
    def test_select_all(self):
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
            ler_todos_usuarios(self.mock_db_config.get("bd")), retorno_esperado
        )


"""     def test_filtro_nome(self):
        retorno_esperado = [(1, "Carla F.", "c@c.com")]
        print(
            ler_usuario_nome(self.mock_db_config.get("bd"), "Carla F."),
        )
        self.assertEqual(
            ler_usuario_nome(self.mock_db_config.get("bd"), "Carla F."),
            retorno_esperado,
        )

    def test_order_by(self):
        retorno_esperado = [
            (3, "sabonete", 8569, "higiene", 2, 5),
            (4, "leite", 5214, "laticinios", 5, 4),
            (2, "agua sanitaria", 3211, "limpeza", 7.5, 2),
            (1, "sabao", 5598, "limpeza", 20.00, 3),
        ]
        self.assertEqual(ler_produtos(self.mock_db_config.get("bd")), retorno_esperado) """

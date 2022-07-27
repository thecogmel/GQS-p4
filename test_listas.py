from listas import *
import unittest


class TestMenorElementoLista(unittest.TestCase):
    def test_valores_entrada(self):
        self.assertRaises(TypeError, menor_elemento_lista, ["um", 0, 10])
        self.assertRaises(TypeError, menor_elemento_lista, [20.5, 1, True])

    def test_reposicao_q1(self):
        self.assertEqual(
            reposicao_q1([("Shampoo", 10), ("Condicionador", 5), ("Sabonete", 2)]),
            1,
        )

    def test_percent_venda_q2(self):
        self.assertEqual(
            venda_q2([(1, 1, 4), (1, 2, 3), (1, 3, 1), (2, 1, 3)]),
            [(1, 0.6364), (2, 0.2727), (3, 0.0909)],
        )

    def test_sum_q3(self):
        self.assertEqual(
            sum_q3([(1, 50.50), (2, 200.95), (3, 20.95), (4, 100.40)]),
            (372.8),
        )

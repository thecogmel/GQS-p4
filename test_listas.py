from listas import *
import unittest


class TestUnitariosGQS4(unittest.TestCase):
    def test_alunos_matriculados(self):
        self.assertEqual(
            alunos_matriculados([[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]], 1), (3)
        )

    def test_turma_matriculado(self):
        self.assertEqual(
            turma_matriculada([[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]], 1), (2)
        )

    def teste_maior_turma(self):
        self.assertEqual(maior_turma([[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]), (1))

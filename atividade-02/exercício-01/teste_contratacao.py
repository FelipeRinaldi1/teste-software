import unittest
from contratacao import verificar_contratacao

class TestContratacaoV3(unittest.TestCase):

    def test_classes_equivalencia(self):
        self.assertEqual(verificar_contratacao(-5), "Entrada Inválida")
        self.assertEqual(verificar_contratacao(10), "Não empregar")
        self.assertEqual(verificar_contratacao(16), "Pode ser empregado tempo parcial")
        self.assertEqual(verificar_contratacao(30), "Pode ser empregado tempo integral")
        self.assertEqual(verificar_contratacao(70), "Não empregar")
        self.assertEqual(verificar_contratacao(100), "Entrada Inválida")

    def test_valores_limite(self):
        self.assertEqual(verificar_contratacao(0), "Não empregar")
        self.assertEqual(verificar_contratacao(15), "Não empregar")
        self.assertEqual(verificar_contratacao(16), "Pode ser empregado tempo parcial")
        self.assertEqual(verificar_contratacao(17), "Pode ser empregado tempo parcial")
        self.assertEqual(verificar_contratacao(18), "Pode ser empregado tempo integral")
        self.assertEqual(verificar_contratacao(54), "Pode ser empregado tempo integral")
        self.assertEqual(verificar_contratacao(55), "Não empregar")
        self.assertEqual(verificar_contratacao(98), "Não empregar")
        self.assertEqual(verificar_contratacao(99), "Entrada Inválida")

if __name__ == '__main__':
    unittest.main()

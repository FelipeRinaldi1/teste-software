import unittest
from grafo import calcular_e1

class TestGrafoCausaEfeito(unittest.TestCase):
    def test_e1_verdadeiro(self):
        self.assertTrue(calcular_e1(True, True))
        self.assertTrue(calcular_e1(True, False))
        self.assertTrue(calcular_e1(False, False))

    def test_e1_falso(self):
        self.assertFalse(calcular_e1(False, True))

if __name__ == "__main__":
    unittest.main()

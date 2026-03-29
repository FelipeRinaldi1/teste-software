import unittest
from calculador_frete import calcular_frete_gratis

class TestPromocao(unittest.TestCase):
    def test_mesma_cidade(self):
        self.assertTrue(calcular_frete_gratis(True, 0, 0.0))
        self.assertTrue(calcular_frete_gratis(True, 5, 500.0))

    def test_outra_cidade_gratis(self):
        self.assertTrue(calcular_frete_gratis(False, 4, 200.0))
        self.assertTrue(calcular_frete_gratis(False, 10, 300.0))

    def test_outra_cidade_pago(self):
        self.assertFalse(calcular_frete_gratis(False, 3, 200.0))
        self.assertFalse(calcular_frete_gratis(False, 4, 199.99))
        self.assertFalse(calcular_frete_gratis(False, 2, 50.0))

if __name__ == "__main__":
    unittest.main()
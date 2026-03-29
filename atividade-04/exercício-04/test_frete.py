import unittest
from frete import calcular_frete_gratis

class TestFrete(unittest.TestCase):
    def test_regra_mesma_cidade(self):
        self.assertTrue(calcular_frete_gratis(True, 1, 10.0))

    def test_regra_outra_cidade_sucesso(self):
        self.assertTrue(calcular_frete_gratis(False, 4, 200.0))

    def test_regra_outra_cidade_falha_qtd(self):
        self.assertFalse(calcular_frete_gratis(False, 3, 250.0))

    def test_regra_outra_cidade_falha_valor(self):
        self.assertFalse(calcular_frete_gratis(False, 5, 199.99))

if __name__ == "__main__":
    unittest.main()
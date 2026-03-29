import unittest
from contratacao import avaliar_contratacao

class TestContratacao(unittest.TestCase):
    def test_faixas_negativas(self):
        self.assertEqual(avaliar_contratacao(15), "Não empregar")
        self.assertEqual(avaliar_contratacao(70), "Não empregar")

    def test_tempo_parcial(self):
        self.assertEqual(avaliar_contratacao(16), "Pode ser empregado tempo parcial")
        self.assertEqual(avaliar_contratacao(17), "Pode ser empregado tempo parcial")

    def test_tempo_integral(self):
        self.assertEqual(avaliar_contratacao(18), "Pode ser empregado tempo integral")
        self.assertEqual(avaliar_contratacao(54), "Pode ser empregado tempo integral")

    def test_limites_invalidos(self):
        self.assertEqual(avaliar_contratacao(-1), "Erro: Idade inválida")
        self.assertEqual(avaliar_contratacao(100), "Erro: Idade inválida")

if __name__ == "__main__":
    unittest.main()
import unittest
from classificacao_cliente import verificar_vip

class TestClassificacaoCliente(unittest.TestCase):

    def test_regra_t1_vip(self):
        self.assertEqual(verificar_vip(2, 2000), "Sim")
        self.assertEqual(verificar_vip(5, 5000), "Sim")

    def test_regras_nao_vip(self):
        self.assertEqual(verificar_vip(2, 1999.99), "Não") # T2
        self.assertEqual(verificar_vip(1, 3000), "Não")    # T3
        self.assertEqual(verificar_vip(0, 0), "Não")       # T4

    def test_entradas_invalidas(self):
        self.assertEqual(verificar_vip(-1, 2000), "Erro: Valores Negativos")
        self.assertEqual(verificar_vip(2, "2000"), "Erro: Entrada Inválida")

if __name__ == '__main__':
    unittest.main()
import unittest
from venda_autorizada import verificar_permissao_venda

class TestVendaAutorizada(unittest.TestCase):

    def test_regra_t1_maioridade(self):
        self.assertEqual(verificar_permissao_venda(18), "Sim")
        self.assertEqual(verificar_permissao_venda(25), "Sim")

    def test_regra_t2_menoridade(self):
        self.assertEqual(verificar_permissao_venda(17), "Não")
        self.assertEqual(verificar_permissao_venda(0), "Não")

    def test_entradas_invalidas(self):
        self.assertEqual(verificar_permissao_venda(-1), "Entrada Inválida")
        self.assertEqual(verificar_permissao_venda(150), "Entrada Inválida")
        self.assertEqual(verificar_permissao_venda("18"), "Entrada Inválida")

if __name__ == '__main__':
    unittest.main()
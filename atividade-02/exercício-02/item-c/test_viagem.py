import unittest
from validacao_viagem import verificar_permissao_viagem

class TestValidacaoViagem(unittest.TestCase):

    def test_regras_tabela_decisao(self):
        self.assertEqual(verificar_permissao_viagem(20, True, True), "Sim")
        self.assertEqual(verificar_permissao_viagem(25, True, False), "Sim")
        self.assertEqual(verificar_permissao_viagem(30, False, True), "Não")
        self.assertEqual(verificar_permissao_viagem(19, False, False), "Não")

        self.assertEqual(verificar_permissao_viagem(10, True, True), "Sim")
        self.assertEqual(verificar_permissao_viagem(15, True, False), "Não")
        self.assertEqual(verificar_permissao_viagem(12, False, True), "Não")
        self.assertEqual(verificar_permissao_viagem(17, False, False), "Não")

    def test_entrada_invalida(self):
        self.assertEqual(verificar_permissao_viagem(-1, True, True), "Erro: Entrada Inválida")

if __name__ == '__main__':
    unittest.main()

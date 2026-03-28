import unittest
from validacao_viagem import verificar_permissao_viagem

class TestValidacaoViagem(unittest.TestCase):

    def test_regras_tabela_decisao(self):
        # T1: Maior, Com Passaporte, Com Responsável -> Sim
        self.assertEqual(verificar_permissao_viagem(20, True, True), "Sim")
        
        # T2: Maior, Com Passaporte, Sem Responsável -> Sim
        self.assertEqual(verificar_permissao_viagem(25, True, False), "Sim")
        
        # T3: Maior, Sem Passaporte, Com Responsável -> Não
        self.assertEqual(verificar_permissao_viagem(30, False, True), "Não")
        
        # T4: Maior, Sem Passaporte, Sem Responsável -> Não
        self.assertEqual(verificar_permissao_viagem(19, False, False), "Não")

        # T5: Menor, Com Passaporte, Com Responsável -> Sim
        self.assertEqual(verificar_permissao_viagem(10, True, True), "Sim")
        
        # T6: Menor, Com Passaporte, Sem Responsável -> Não
        self.assertEqual(verificar_permissao_viagem(15, True, False), "Não")
        
        # T7: Menor, Sem Passaporte, Com Responsável -> Não
        self.assertEqual(verificar_permissao_viagem(12, False, True), "Não")
        
        # T8: Menor, Sem Passaporte, Sem Responsável -> Não
        self.assertEqual(verificar_permissao_viagem(17, False, False), "Não")

    def test_entrada_invalida(self):
        self.assertEqual(verificar_permissao_viagem(-1, True, True), "Erro: Entrada Inválida")

if __name__ == '__main__':
    unittest.main()
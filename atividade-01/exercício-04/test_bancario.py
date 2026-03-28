import unittest
from interface_bancaria import processar_operacao

class TestInterfaceBancaria(unittest.TestCase):

    def test_classes_equivalencia(self):
        # Caso Válido Completo
        self.assertEqual(processar_operacao("011", "344", "2598", "abc123", "c"), "Operação Cheque autorizada")
        # Cód Área Vazio (Válido)
        self.assertEqual(processar_operacao("", "555", "1234", "user01", "d"), "Operação Depósito autorizada")
        # Erro Prefixo inicia com zero
        self.assertEqual(processar_operacao("011", "044", "2598", "abc123", "e"), "Erro: Prefixo inválido")
        # Erro Senha caracteres especiais
        self.assertEqual(processar_operacao("011", "344", "2598", "abc@12", "c"), "Erro: Senha inválida")

    def test_valores_limite(self):
        # Sufixo com 3 e 5 dígitos
        self.assertEqual(processar_operacao("011", "344", "259", "abc123", "c"), "Erro: Sufixo inválido")
        self.assertEqual(processar_operacao("011", "344", "25987", "abc123", "c"), "Erro: Sufixo inválido")
        # Senha com 5 e 7 dígitos
        self.assertEqual(processar_operacao("011", "344", "2598", "abc12", "c"), "Erro: Senha inválida")
        self.assertEqual(processar_operacao("011", "344", "2598", "abc1234", "c"), "Erro: Senha inválida")

if __name__ == '__main__':
    unittest.main()
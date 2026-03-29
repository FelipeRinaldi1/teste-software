import unittest
from operacao_bancaria import validar_operacao_bancaria

class TestInterfaceBancaria(unittest.TestCase):
    def test_sucesso_com_ddd(self):
        self.assertTrue(validar_operacao_bancaria("011", "344", "2598", "abc123", "c"))

    def test_sucesso_ddd_vazio(self):
        self.assertTrue(validar_operacao_bancaria("", "344", "2598", "abc123", "e"))

    def test_falha_cod_area(self):
        self.assertFalse(validar_operacao_bancaria("11", "344", "2598", "abc123", "d"))
        self.assertFalse(validar_operacao_bancaria("111", "344", "2598", "abc123", "d"))

    def test_falha_prefixo(self):
        self.assertFalse(validar_operacao_bancaria("011", "044", "2598", "abc123", "c"))

    def test_falha_sufixo(self):
        self.assertFalse(validar_operacao_bancaria("011", "344", "259", "abc123", "c"))

    def test_falha_senha(self):
        self.assertFalse(validar_operacao_bancaria("011", "344", "2598", "abc12", "c"))

    def test_falha_operacao(self):
        self.assertFalse(validar_operacao_bancaria("011", "344", "2598", "abc123", "x"))

if __name__ == "__main__":
    unittest.main()
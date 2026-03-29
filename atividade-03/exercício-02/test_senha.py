import unittest
from verifica_senha import verificar_senha_forte

class TestVerificaSenha(unittest.TestCase):
    def test_senha_valida(self):
        self.assertTrue(verificar_senha_forte("Senha@123"))

    def test_falha_tamanho(self):
        self.assertFalse(verificar_senha_forte("S@123"))

    def test_falha_maiuscula(self):
        self.assertFalse(verificar_senha_forte("senha@123"))

    def test_falha_minuscula(self):
        self.assertFalse(verificar_senha_forte("SENHA@123"))

    def test_falha_numero(self):
        self.assertFalse(verificar_senha_forte("Senha@abc"))

    def test_falha_simbolo(self):
        self.assertFalse(verificar_senha_forte("Senha123"))

if __name__ == "__main__":
    unittest.main()
import unittest
from validador_senha import validar_senha

class TestValidadorEspecial(unittest.TestCase):
    def test_senha_valida(self):
        self.assertTrue(validar_senha("Senha123"))
        self.assertTrue(validar_senha("?abcde"))

    def test_falha_tamanho(self):
        self.assertFalse(validar_senha("12345"))
        self.assertFalse(validar_senha("SenhaMuitoLonga"))

    def test_falha_primeiro_caractere(self):
        self.assertFalse(validar_senha("@senha123"))
        self.assertFalse(validar_senha("#123456"))

    def test_falha_caractere_controle(self):
        self.assertFalse(validar_senha("Senha\n123"))

    def test_falha_dicionario(self):
        self.assertFalse(validar_senha("Teste"))
        self.assertFalse(validar_senha("software"))

if __name__ == "__main__":
    unittest.main()
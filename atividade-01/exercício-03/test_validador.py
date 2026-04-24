import unittest
from validador_senha import verificar_senha

class TestValidadorV2(unittest.TestCase):

    def test_classes_equivalencia(self):
        self.assertEqual(verificar_senha("Senha123"), "Senha Válida")
        self.assertEqual(verificar_senha("?abcde"), "Senha Válida")
        self.assertEqual(verificar_senha("123456"), "Senha Válida")
        self.assertEqual(verificar_senha("abc"), "Erro: Tamanho inválido (deve ser 6-10)")
        self.assertEqual(verificar_senha("#abcde"), "Erro: Primeiro caractere inválido")
        self.assertEqual(verificar_senha("funcional"), "Erro: Senha consta na lista de termos restritos")

    def test_valores_limite(self):
        self.assertEqual(verificar_senha("12345"), "Erro: Tamanho inválido (deve ser 6-10)")
        self.assertEqual(verificar_senha("123456"), "Senha Válida")
        self.assertEqual(verificar_senha("1234567890"), "Senha Válida")
        self.assertEqual(verificar_senha("12345678901"), "Erro: Tamanho inválido (deve ser 6-10)")

if __name__ == '__main__':
    unittest.main()

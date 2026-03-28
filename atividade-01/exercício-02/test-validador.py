import unittest

from validador_senha import verificar_senha_forte

class TestValidadorSenha(unittest.TestCase):

    def test_classes_equivalencia(self):
        self.assertEqual(verificar_senha_forte("Ab1@5678"), "Senha Forte")
        self.assertEqual(verificar_senha_forte("Ab1@5"), "Senha Fraca: Mínimo 8 caracteres")
        self.assertEqual(verificar_senha_forte("ab1@5678"), "Senha Fraca: Falta letra maiúscula")
        self.assertEqual(verificar_senha_forte("AB1@5678"), "Senha Fraca: Falta letra minúscula")
        self.assertEqual(verificar_senha_forte("Abc@efgh"), "Senha Fraca: Falta número")
        self.assertEqual(verificar_senha_forte("Ab125678"), "Senha Fraca: Falta símbolo")
        self.assertEqual(verificar_senha_forte(12345678), "Entrada Inválida")

    def test_valores_limite(self):
        self.assertEqual(verificar_senha_forte("Ab1@567"), "Senha Fraca: Mínimo 8 caracteres")
        self.assertEqual(verificar_senha_forte("Ab1@5678"), "Senha Forte")
        self.assertEqual(verificar_senha_forte("Ab1@56789"), "Senha Forte")
        self.assertEqual(verificar_senha_forte(""), "Senha Fraca: Mínimo 8 caracteres")

if __name__ == '__main__':
    unittest.main()
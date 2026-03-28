import unittest
from contratacao import verificar_contratacao

class TestContratacao(unittest.TestCase):

    #Particionamento de Equivalência
    def test_classes_equivalencia(self):
        self.assertEqual(verificar_contratacao(-1), "Entrada Inválida")
        self.assertEqual(verificar_contratacao(10), "Não empregar")
        self.assertEqual(verificar_contratacao(16), "Pode ser empregado tempo parcial")
        self.assertEqual(verificar_contratacao(35), "Pode ser empregado tempo integral")
        self.assertEqual(verificar_contratacao(60), "Não empregar")
        self.assertEqual(verificar_contratacao(100), "Entrada Inválida")

    #Valor Limite
    def test_valores_limite(self):
        # Fronteira 15/16
        self.assertEqual(verificar_contratacao(15), "Não empregar")
        self.assertEqual(verificar_contratacao(16), "Pode ser empregado tempo parcial")
        # Fronteira 17/18
        self.assertEqual(verificar_contratacao(17), "Pode ser empregado tempo parcial")
        self.assertEqual(verificar_contratacao(18), "Pode ser empregado tempo integral")
        # Fronteira 54/55
        self.assertEqual(verificar_contratacao(54), "Pode ser empregado tempo integral")
        self.assertEqual(verificar_contratacao(55), "Não empregar")
        # Extremos
        self.assertEqual(verificar_contratacao(0), "Não empregar")
        self.assertEqual(verificar_contratacao(99), "Não empregar")

if __name__ == '__main__':
    unittest.main()
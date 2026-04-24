import unittest
from function_m import m

class TestFunctionM(unittest.TestCase):
    def test_obj_none(self):
        self.assertIsNone(m(10, None))

    def test_odd_i(self):
        self.assertEqual(m(3, 10), 40)

    def test_even_i(self):
        self.assertEqual(m(2, 5), 10)

    def test_negative_i(self):
        self.assertEqual(m(-1, 10), 0)

if __name__ == '__main__':
    unittest.main()

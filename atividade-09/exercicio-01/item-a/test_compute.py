import unittest
from compute import compute

class TestCompute(unittest.TestCase):
    def test_y_is_zero(self):
        self.assertEqual(compute(10, 0), "y is zero")

    def test_x_is_zero(self):
        self.assertEqual(compute(0, 5), "x is zero")

    def test_multiples(self):
        self.assertEqual(compute(5, 2), [2, 4])

    def test_no_multiples(self):
        self.assertEqual(compute(1, 2), [])

if __name__ == '__main__':
    unittest.main()

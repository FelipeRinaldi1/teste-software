import unittest
from contains import contains

class TestContains(unittest.TestCase):
    def test_empty_interval(self):
        self.assertEqual(contains(5, 10, 1), ["the interval is empty"])

    def test_interior_point(self):
        self.assertEqual(contains(5, 2, 8), ["x is an interior point"])

    def test_outside_low(self):
        self.assertEqual(contains(0, 2, 8), ["x is outside the interval"])

    def test_outside_high(self):
        self.assertEqual(contains(10, 2, 8), ["x is outside the interval"])

    def test_boundary_low(self):
        self.assertEqual(contains(2, 2, 8), ["x is an interior point", "x is outside the interval"])

    def test_boundary_high(self):
        self.assertEqual(contains(8, 2, 8), ["x is an interior point", "x is outside the interval"])

if __name__ == '__main__':
    unittest.main()

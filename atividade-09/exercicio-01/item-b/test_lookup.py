import unittest
from lookup import lookup

class TestLookup(unittest.TestCase):
    def test_found_at_middle(self):
        vec = [1, 3, 5, 7, 9]
        self.assertEqual(lookup(vec, 5, 4), 2)

    def test_found_lower(self):
        vec = [1, 3, 5, 7, 9]
        self.assertEqual(lookup(vec, 1, 4), 0)

    def test_found_upper(self):
        vec = [1, 3, 5, 7, 9]
        self.assertEqual(lookup(vec, 9, 4), 4)

    def test_not_found(self):
        vec = [1, 3, 5, 7, 9]
        self.assertEqual(lookup(vec, 4, 4), -1)

if __name__ == '__main__':
    unittest.main()

import unittest
from do_something import do_something

class TestDoSomething(unittest.TestCase):
    def test_x_gt_100(self):
        self.assertEqual(do_something(101, [0]), ("less than 100", "f", "ff"))

    def test_x_le_100_y_becomes_vec0_case2(self):
        self.assertEqual(do_something(50, [2]), ("", "g", "ff"))

    def test_x_le_0_y_becomes_vec0_case1(self):
        self.assertEqual(do_something(0, [1]), ("", "f", "ff"))

    def test_y_other(self):
        self.assertEqual(do_something(0, [3]), ("", None, "ff"))

if __name__ == '__main__':
    unittest.main()

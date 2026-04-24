import unittest
from coverage_example import example1, ErrorCodes

class TestCoverageExample(unittest.TestCase):
    def test_condition_true(self):
        example1(True, "test", ErrorCodes.EACCES, ['a', '\0'])

    def test_condition_false_equal_strings(self):
        example1(False, None, ErrorCodes.ENODEV, ['b', '\0'])

    def test_condition_false_not_equal_strings(self):
        example1(False, "x", ErrorCodes.ENOENT, ['c', '\0'])

    def test_index_error(self):
        example1(True, "test", ErrorCodes.EACCES, ['a'])

if __name__ == '__main__':
    unittest.main()

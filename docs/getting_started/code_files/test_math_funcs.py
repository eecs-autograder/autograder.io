import unittest
import math_funcs

class MathFuncTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(11, math_funcs.add(8, 3))

    def test_subtract(self):
        self.assertEqual(-3, math_funcs.subtract(5, 8))

    def test_multiply(self):
        self.assertEqual(42, math_funcs.multiply(7, 6))

if __name__ == '__main__':
    unittest.main()

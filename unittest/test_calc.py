import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        # old way:
        result = calc.add(10, 5)
        self.assertEqual(result, 15)
        # better one:
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)
        self.assertEqual(calc.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
        self.assertEqual(calc.multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # old way:
        self.assertRaises(ValueError, calc.divide, 10, 0)

        # or with context manager:
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()

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

    def test_substract(self):
        self.assertEqual(calc.substract(-1, 1), -2)
        self.assertEqual(calc.substract(-1, -1), 0)
        self.assertEqual(calc.substract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
        self.assertEqual(calc.multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(5, 2), 2.5)
        self.assertEqual(calc.divide(10, 0), 2)

        self.assertRaises(calc.divide(10, 0), 2)


if __name__ == '__main__':
    unittest.main()

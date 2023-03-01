"""
From URL: https://www.youtube.com/watch?v=6tNS--WetLI&t=1102s
"""

import unittest
from employee import Employee


class TeatEmployee(unittest.TestCase):

    def test_email(self):
        """
        Purpose: testing changes of property email
        """
        emp_1 = Employee('Suzan', 'Vega', 200000)
        emp_2 = Employee('Tom', 'Clancy', 1000000)

        self.assertEqual(emp_1.email, 'Suzan.Vega@email.com')
        self.assertEqual(emp_2.email, 'Tom.Clancy@email.com')

        emp_1.first = 'Thomas'
        emp_2.last = 'Johns'

        self.assertEqual(emp_1.email, 'Thomas.Vega@email.com')
        self.assertEqual(emp_2.email, 'Tom.Johns@email.com')

    def test_fullname(self):
        """
        Purpose: testing changes of property fullname
        """
        emp_1 = Employee('Suzan', 'Vega', 200000)
        emp_2 = Employee('Tom', 'Clancy', 1000000)

        self.assertEqual(emp_1.fullname, 'Suzan Vega')
        self.assertEqual(emp_2.fullname, 'Tom Clancy')

        emp_1.first = 'Thomas'
        emp_2.last = 'Johns'

        self.assertEqual(emp_1.fullname, 'Thomas Vega')
        self.assertEqual(emp_2.fullname, 'Tom Johns')

    def test_apply_raise(self):
        """
        Purpose: testing changes of property fullname
        """
        emp_1 = Employee('Suzan', 'Vega', 200000)
        emp_2 = Employee('Tom', 'Clancy', 1000000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 210000)
        self.assertEqual(emp_2.pay, 1050000)


if __name__ == '__main__':
    unittest.main()

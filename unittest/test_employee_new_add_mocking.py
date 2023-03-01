"""
From URL: https://www.youtube.com/watch?v=6tNS--WetLI&t=1102s
"""

import unittest
from unittest.mock import patch # can be used as decorator or context manager
from employee import Employee


class TeatEmployeeNewMocking(unittest.TestCase):

    # add setUp and tearDown classes that will run only once before and after all tests
    @classmethod
    def setUpClass(cls):
        """
        Purpose: run only once, before and after all tests
        """
        print(f' >-> setUpClass')
        pass

    @classmethod
    def tearDownClass(cls):
        """
        Purpose: run only once, before and after all tests
        """
        print('\n >-> tearDownClass')
        pass

    def setUp(self):
        """
        Purpose: Runs before every single test
        """
        print(f'\n  >>--> setUp')
        self.emp_1 = Employee('Suzan', 'Vega', 200000)
        self.emp_2 = Employee('Tom', 'Clancy', 1000000)

    def tearDown(self):
        """
        Purpose: Runs after every single test
        """
        print('  >>--> tearDown')
        pass

    def test_email(self):
        """
        Purpose: testing changes of property email
        """
        print('   >>>---> test_email')

        self.emp_1.first = 'Thomas'
        self.emp_2.last = 'Johns'

        self.assertEqual(self.emp_1.email, 'Thomas.Vega@email.com')
        self.assertEqual(self.emp_2.email, 'Tom.Johns@email.com')

    def test_fullname(self):
        """
        Purpose: testing changes of property fullname
        """
        print('   >>>---> test_fullname')

        self.assertEqual(self.emp_1.fullname, 'Suzan Vega')
        self.assertEqual(self.emp_2.fullname, 'Tom Clancy')

        self.emp_1.first = 'Thomas'
        self.emp_2.last = 'Johns'

        self.assertEqual(self.emp_1.fullname, 'Thomas Vega')
        self.assertEqual(self.emp_2.fullname, 'Tom Johns')

    def test_apply_raise(self):
        """
        Purpose: testing changes of property fullname
        """
        print('    >>>---> test_apply_raise')

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 210000)
        self.assertEqual(self.emp_2.pay, 1050000)

    def test_monthly_schedule(self):
        """
        Purpose: Testing mocked requests for monthly_schedule
        with use under employee.py

        def monthly_schedule(self, month):
            response = requests.get(f'https://company.com/{self.last}/{month}')
            if response.ok:
                return response.text
            else:
                return 'Bad Response!'
        """
        with patch('employee.requests.get') as mocked_get:
            # For working ok = True
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('https://company.com/Vega/May')
            self.assertEquals(schedule, 'Success')

            # For working ok = True
            mocked_get.return_value.ok = False
            
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('https://company.com/Clancy/June')
            self.assertEquals(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()

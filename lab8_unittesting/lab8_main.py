"""
Makhai Morgan
Lab 8, unittest
Sep 29, 2025
Oct 6, 2025
"""

import unittest
import calculation
from employee import Employee  # import class 'Employee' from 'employee'py'


# function to add and return the sum of two numbers
def addtwonumbers(a, b):
    return a + b


print("\n---- Example 1: test for equality ----- ")


# crerate a code to test function 'addtwonumbers'
class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addtwonumbers(2, 3), 5)


print("\n---- Example 2: unittest for calculations ----- ")


class TestCalculation(unittest.TestCase):
    def test_multiplications(self):
        self.assertEqual(calculation.multplythreenumbers(5), 5)
        self.assertEqual(calculation.multplythreenumbers(2, 3), 6)
        self.assertEqual(calculation.multplythreenumbers(0), 0)

    def test_division(self):
        self.assertEqual(calculation.dividetwonumbers(8, 4), 2)
        self.assertAlmostEqual(calculation.dividetwonumbers(9, 2), 4.5)
        self.assertEqual(calculation.dividetwonumbers(0, 9), 0)
        self.assertIsNone(calculation.dividetwonumbers("a", 2))

    def test_addition(self):
        self.assertEqual(calculation.addthreenumbers(7, 6), 13)
        self.assertEqual(calculation.addthreenumbers(5, 4), 9)
        self.assertEqual(calculation.addthreenumbers(8, 4), 12)


print("\n---- Example 3: unittest for Employee ----- ")


class TestEmplyoee(unittest.TestCase):
    # create a test templte
    def setUp(self):
        # create an instant of a new employee
        self.emp1 = Employee("Peter", "Pan", 50000)

    # create a test for employee email
    def test_emailemployee(self):
        self.assertEqual(self.emp1.emailemployee, "Peter.Pan@email.com")

    # create a test for emplyoee full
    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, "Peter Pan")

        # update the first name
        self.emp1.first = "Will"

        # re-test full name
        self.assertEqual(self.emp1.fullname, "Will Pan")

    # create a test for salary
    def test_salary(self):
        # test salary before the raise
        self.assertEqual(self.emp1.salary, 50000)

        # first, raise the salry first
        self.emp1.apply_raise()

        # second, test salary
        self.assertEqual(self.emp1.salary, 52500)


print("\n---- LAB EXERCISE: Bank Account ----- ")


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # Creating default Bank Account instance
        self.account1 = TestBankAccount("Jordan Keuring", 3489, 50)

    def test_initial_balance(self):
        # Bank account balance initialization
        self.assertEqual(self.account1.get_balance(), 50)

    def test_deposit(self):
        # Test that deposit adds to the balance
        self.account1.deposit(125)
        self.assertEqual(self.account1.get_balance(), 175)  # 50 +1 25 = 175

    def test_withdraw(self):
        # Test that withdraw subtracts from balance
        self.account1.withdraw(30)
        self.assertEqual(self.account1.get_balance(), 20)  # 50 - 30 = 20

    def test_withdraw_more_than_balance(self):
        # Test that withdrawing more than the balance amount raises ValueError
        with self.assertRaises(ValueError):
            self.account1.withdraw(70)

    def test_sequence_of_transactions(self):
        # Testing a series of deposit and withdrawals
        self.account1.deposit(100)  # Balance: 150
        self.account1.withdraw(50)  # Balance: 100
        self.account1.deposit(25)  # Balance: 125
        self.account1.withdraw(75)  # Balance: 50


if __name__ == "__main__":
    unittest.main()

"""
Makhai Morgan
Lab 8, unittest
Sep 29, 2025
"""
import unittest
import calculations
# function to add and return the sum of two numbers
def addtwonumbers(a,b):
    return a+b

print("\n---- Example 1: test for equality ----- ")
# crerate a code to test function 'addtwonumbers'
class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addtwonumbers(2,3),5)

print("\n---- Example 2: unittest for calculations ----- ")
class TestCalculation(unittest.TestCase):
    def test_multiplications(self):
        self.assertEqual(calculations.multiplythreenumbers(5),5)
        self.assertEqual(calculations.multiplythreenumbers(2,3),6)
        self.assertEqual(calculations.multiplythreenumbers(0),0)


    def test_division(self):
        self.assertEqual(calculations.dividitwonumbers(8,4),2)
        self.assertAlmostEqual(calculations.dividitwonumbers(9,2),4)
        self.assertEqual(calculations.dividitwonumbers(9,0),-1)
        self.assertIsNone(calculations.dividitwonumbers("a",2))

    def test_addition(self):
        self.assertEqual(calculations.addtwonumbers(7,6),2)
        self.assertEqual(calculations.)
if __name__ =="__main__":
    unittest.main()
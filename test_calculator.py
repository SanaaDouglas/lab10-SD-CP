
# https://github.com/SanaaDouglas/lab10-SD-CP
#Partner 1: Sanaa Douglas
#Partner 2: Chase Prasad

import unittest
from calculator import mul, div, logarithm, hypotenuse, square_root
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        pass

    def test_subtract(self): # 3 assertions
        pass
    ##########################

    # Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3,4), 12)
        self.assertEqual(mul(4, 5), 20)
        self.assertEqual(mul(5,5), 25)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(20,5), 4)
        self.assertEqual(div(12,3) , 4)
        self.assertEqual(div(10, 2), 5)
    ##########################

    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        pass

    def test_logarithm(self): # 3 assertions
        pass
    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        pass
    ##########################
    
    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(0,5)
        with self.assertRaises(ValueError):
            logarithm(-3, 2)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(25), 5)
        with self.assertRaises(ValueError):
            square_root(-4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
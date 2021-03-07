import unittest
import calculator

class TestCalc(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(calculator.sum(5, 2), 7)
    
    def test_minus(self):
        self.assertEqual(calculator.minus(5, 2), 3)
    
    def test_div(self):
        self.assertEqual(calculator.div(6, 2), 3.0)
        self.assertRaises(ZeroDivisionError, calculator.div, 6, 0)
    
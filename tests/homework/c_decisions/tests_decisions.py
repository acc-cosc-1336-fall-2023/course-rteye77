import unittest
from src.homework.d_repetition.repetition import sum_odd_numbers
class Test_Config(unittest.TestCase):
    
    def test_sum_odd_numbers(self):
        self.assertEqual(25, sum_odd_numbers(9))
        self.assertEqual(25, sum_odd_numbers(10))
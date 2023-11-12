#
import unittest
from src.homework.j_classes.class_a import Die

baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

class Test_Config(unittest.TestCase):

    def test_get_rolled_value(self):
        die = Die()
        die.roll()
        rolled_value = die.get_rolled_value()
        self.assertTrue(1 <= rolled_value <= 6)
    def test_get_rolled_value2(self):
        die1 = Die()
        die1.roll()
        rolled_value = die1.get_rolled_value()
        self.assertTrue(1 <= rolled_value <= 6)
    def test_get_rolled_value3(self):
        die2 = Die()
        die2.roll()
        rolled_value = die2.get_rolled_value()
        self.assertTrue(1 <= rolled_value <= 6)
        
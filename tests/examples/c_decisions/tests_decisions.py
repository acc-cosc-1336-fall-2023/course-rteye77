import unittest
from homework.c_decisions.decisions import get_letter_grade

from src.examples.c_decisions.decisions import test_config

class Test_Config(unittest.TestCase):

    def test_get_options_ratio (self):
        self.assertEquals(0.25, get_option_ratio (5,20))
        self.assertEquals(0.50, get_option_ratio (10,20))

    def test_get_faculty_rating (self):
        self.assertEqual(get_faculty_rating (0.91), "Excellent")
        self.assertEqual(get_faculty_rating (0.85), "Very Good")
        self.assertEqual(get_faculty_rating (0.71), "Good")
        self.assertEqual(get_faculty_rating (0.66), "Needs Improvement")
        self.assertEqual(get_faculty_rating 0.45) "Unacceptable")
        self.assertEqual(get_faculty_rating (-1), "Invalid Rating")                                 



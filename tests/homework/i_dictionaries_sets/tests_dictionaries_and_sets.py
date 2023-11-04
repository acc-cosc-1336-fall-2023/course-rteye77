#
import unittest
from src.homework.h_strings.strings import get_hamming_distance
from src.homework.h_strings.strings import get_dna_complement
from src.homework.i_dictionaries_sets.dictionary import add_inventory
from src.homework.i_dictionaries_sets.dictionary import remove_inventory_widget

baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

class Test_Config(unittest.TestCase):

    def test_get_hamming_distance(self):
         self.assertEqual(get_hamming_distance("GAGCCTACTAACGGGAT","CATCGTAATGACGGCCT"),7)
        
    def test_get_dna_complement(self):
         self.assertEqual(get_dna_complement ("AAAACCCGGT"),"ACCGGGTTTT")
    
    def test_add_inventory(self):
         inventory = {}
         add_inventory(inventory, "Widget1", 10)
         self.assertEqual(inventory["Widget1"], 10)
         add_inventory(inventory, "Widget1", 25)
         self.assertEqual(inventory["Widget1"], 35)
         add_inventory(inventory, "Widget1", -10)
         self.assertEqual(inventory["Widget1"], 25)
    
    def test_remove_inventory_widget(self):
         inventory = {}
         add_inventory(inventory, "Widget1", 10)
         add_inventory(inventory, "Widget2", 20)
         remove_inventory_widget(inventory, "Widget1")
         self.assertEqual(inventory.__len__(),1)
         self.assertEqual(inventory["Widget2"], 20)
     
    def test_intersection(self):
         intersection_result = baseball.intersection(basketball)
         print("Intersection results:",intersection_result)
     
    def test_union(self):
         union_result = baseball.union(basketball)
         print("Union results:",union_result)

    def test_difference_baseball(self):
         baseball_only = baseball.difference(basketball)
         print("Baseball only results:",baseball_only)
         
    def test_difference_basketball(self):
         basketball_only = basketball.difference(baseball)
         print("Basketball oly results:",basketball_only)
    
    def test_difference_basketball(self):
         symmetric_difference_result = baseball.symmetric_difference(basketball)
         print("Symmetric difference results:",symmetric_difference_result)
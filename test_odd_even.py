import unittest
from odd_even import even,odd



class TestPrintOddEvenNumbers(unittest.TestCase):
    def test_print_only_odd_numbers_as_string(self):
        self.assertEqual(odd([1,2,3,4,5,6,7,8,9]),"1,3,5,7,9")


    def test_print_only_even_numbers_as_string(self):
        self.assertEqual(even([1,2,3,4,5,6,7,8,9]),"2,4,6,8")
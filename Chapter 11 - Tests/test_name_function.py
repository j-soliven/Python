import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Bob Dylan' work?"""
        formatted_name = get_formatted_name('bob', 'dylan')
        self.assertEqual(formatted_name, 'Bob Dylan')

    def test_first_middle_last_name(self):
        """Do names like Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()
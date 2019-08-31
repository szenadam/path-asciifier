import unittest
from src.replacer import Replacer

class TestReplacer(unittest.TestCase):
    def test_replacer_exists(self):
        r = Replacer()
        self.assertIsInstance(r, Replacer)
    
    def test_replace_small_a_chars(self):
        # Arrange
        r = Replacer()
        string_with_a = '\xe0\xe1\xe2\xe3\xe4\xe5'
        # Act
        string_with_a = r.replace(string_with_a)
        # Assert
        self.assertEqual(string_with_a, 'aaaaaa')

    def test_replace_small_e_chars(self):
        r = Replacer()
        string_with_e = '\xe8\xe9\xea\xeb'

        string_with_e = r.replace(string_with_e)

        self.assertEqual(string_with_e, 'eeee')


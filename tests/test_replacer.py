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

    def test_replace_small_i_chars(self):
        r = Replacer()
        string_with_i = '\xec\xed\xee\xef'

        string_with_i = r.replace(string_with_i)

        self.assertEqual(string_with_i, 'iiii')

    def test_replace_small_o_chars(self):
        r = Replacer()
        string_with_o = '\xf2\xf3\xf4\xf5\xf6'

        string_with_o = r.replace(string_with_o)

        self.assertEqual(string_with_o, 'ooooo')
    
    def test_replace_small_u_chars(self):
        r = Replacer()
        string_with_u = '\xf9\xfa\xfb\xfc'

        string_with_u = r.replace(string_with_u)

        self.assertEqual(string_with_u, 'uuuu')

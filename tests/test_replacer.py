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

    def test_replace_upper_a_chars(self):
        # Arrange
        r = Replacer()
        string_with_a = '\xc0\xc1\xc2\xc3\xc4\xc5'
        # Act
        string_with_a = r.replace(string_with_a)
        # Assert
        self.assertEqual(string_with_a, 'AAAAAA')

    def test_replace_small_e_chars(self):
        # Arrange
        r = Replacer()
        string_with_e = '\xe8\xe9\xea\xeb'
        # Act
        string_with_e = r.replace(string_with_e)
        # Assert
        self.assertEqual(string_with_e, 'eeee')

    def test_replace_upper_e_chars(self):
        # Arrange
        r = Replacer()
        string_with_e = '\xc8\xc9\xca\xcb'
        # Act
        string_with_e = r.replace(string_with_e)
        # Assert
        self.assertEqual(string_with_e, 'EEEE')

    def test_replace_small_i_chars(self):
        # Arrange
        r = Replacer()
        string_with_i = '\xec\xed\xee\xef'
        # Act
        string_with_i = r.replace(string_with_i)
        # Assert
        self.assertEqual(string_with_i, 'iiii')

    def test_replace_upper_i_chars(self):
        # Arrange
        r = Replacer()
        string_with_i = '\xcc\xcd\xce\xcf'
        # Act
        string_with_i = r.replace(string_with_i)
        # Assert
        self.assertEqual(string_with_i, 'IIII')

    def test_replace_small_o_chars(self):
        # Arrange
        r = Replacer()
        string_with_o = '\xf2\xf3\xf4\xf5\xf6'
        # Act
        string_with_o = r.replace(string_with_o)
        # Assert
        self.assertEqual(string_with_o, 'ooooo')

    def test_replace_upper_o_chars(self):
        # Arrange
        r = Replacer()
        string_with_o = '\xd2\xd3\xd4\xd5\xd6'
        # Act
        string_with_o = r.replace(string_with_o)
        # Assert
        self.assertEqual(string_with_o, 'OOOOO')
    
    def test_replace_small_u_chars(self):
        # Arrange
        r = Replacer()
        string_with_u = '\xf9\xfa\xfb\xfc'
        # Act
        string_with_u = r.replace(string_with_u)
        # Assert
        self.assertEqual(string_with_u, 'uuuu')

    def test_replace_upper_u_chars(self):
        # Arrange
        r = Replacer()
        string_with_u = '\xd9\xda\xdb\xdc'
        # Act
        string_with_u = r.replace(string_with_u)
        # Assert
        self.assertEqual(string_with_u, 'UUUU')
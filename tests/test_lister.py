import unittest
from unittest import mock 
from src.lister import ListFiles


class TestLister(unittest.TestCase):
    def test_file_lister_exists(self):
        l = ListFiles()
        self.assertIsInstance(l, ListFiles)


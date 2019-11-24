import unittest, os
from unittest import mock
from src.lister import FileLister


class TestLister(unittest.TestCase):
    def test_file_lister_exists(self):
        l = FileLister()
        self.assertIsInstance(l, FileLister)

    def test_lists_files(self):
        l = FileLister()
        
        expected = [os.path.join('.', 'foo'), os.path.join('.', 'bar'), os.path.join('.', 'baz')]
        result = []

        with mock.patch('os.walk') as mockwalk:
            mockwalk.return_value = [('.', None, ('foo', 'bar', 'baz'))]
            result = l.list_files('.')

        self.assertListEqual(result, expected)

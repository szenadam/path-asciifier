import os
import unittest
from unittest import mock

from modules.lister import FileLister


class TestLister(unittest.TestCase):
    def test_file_lister_exists(self):
        # Arrange, Act
        lister = FileLister()
        # Assert
        self.assertIsInstance(lister, FileLister)

    def test_lists_files(self):
        # Arrange
        lister = FileLister()
        expected = [os.path.join('.', i) for i in ['foo', 'bar', 'baz']]
        # Act
        with mock.patch('os.walk') as mockwalk:
            mockwalk.return_value = [('.', None, ('foo', 'bar', 'baz'))]
            result = lister.list_files('.')
        # Assert
        self.assertListEqual(result, expected)

    @unittest.skip("need to fix os.walk mock")
    def test_list_dirs(self):
        # Arrange
        lister = FileLister()
        expected = [os.path.join('.', 'foo'), os.path.join('.', 'bar'), os.path.join('.', 'baz')]
        # Act
        with mock.patch('os.walk') as mockwalk:
            mockwalk.return_value = [('.', 'foo', ())]
            result = lister.list_dirs('.')
        # Arrange
        self.assertListEqual(result, expected)

"""
Jason Chow
A00942129
"""
from unittest import TestCase
from unittest.mock import patch
from utility import clear


# https://itecnote.com/tecnote/python-the-best-way-to-mock-os-system-for-unit-test-pytest/

class TestClear(TestCase):
    @patch('os.system')
    @patch('os.name', 'nt')
    def test_clear_windows(self, mock_system):
        clear()
        mock_system.assert_called_once_with('cls')

    @patch('os.system')
    @patch('os.name', 'posix')
    def test_clear_linux(self, mock_system):
        clear()
        mock_system.assert_called_once_with('clear')

"""
Jason Chow
A00942129
"""
import io
from unittest import TestCase
from unittest.mock import patch

from utility import draw


class TestDraw(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_draw(self, mock_output):
        draw()
        actual = mock_output.getvalue()
        expected = "xX------------------------------------------------------Xx\n"
        self.assertEqual(actual, expected)

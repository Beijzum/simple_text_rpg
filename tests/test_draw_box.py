"""
Jason Chow
A00942129
"""
from unittest import TestCase

from utility import draw_box


class TestDrawBox(TestCase):
    def test_draw_box_with_message(self):
        actual = draw_box("Hello, World!")
        expected = (
            "+▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔+\n"
            "|  Hello, World!  |\n"
            "+▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁+"
        )

        self.assertEqual(actual, expected)

    def test_draw_box_with_empty_message(self):
        actual = draw_box("")
        expected = (
            "+▔▔▔▔+\n"
            "|    |\n"
            "+▁▁▁▁+"
        )
        self.assertEqual(actual, expected)

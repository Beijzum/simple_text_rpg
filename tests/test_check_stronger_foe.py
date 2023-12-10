"""
Jason Chow
A00942129
"""
import io
from unittest import TestCase
from unittest.mock import patch
from exploration import check_stronger_foe
from utility import draw_box


class TestCheckStrongerFoe(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_stronger_foe_detected(self, mock_output):
        character = {
            "Inventory": {
                "1": {"Name": "Frozen Orb"},
                "2": {"Name": "Flame Orb"}
            },
            "Stronger Enemies": False
        }
        check_stronger_foe(character)
        actual = mock_output.getvalue()
        expected = draw_box("You sense the presence of stronger enemies in the dungeon.") + "\n"
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_no_stronger_foe_detected(self, mock_output):
        character = {
            "Inventory": {
                "1": {"Name": "Frozen Orb"},
                "2": {"Name": "Flame Orb"}
            },
            "Stronger Enemies": True
        }
        check_stronger_foe(character)
        actual = mock_output.getvalue()
        expected = ""
        self.assertEqual(expected, actual)

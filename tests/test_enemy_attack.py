"""
Jason Chow
A00942129
"""
import io
from unittest import TestCase
from unittest.mock import patch
from combat import enemy_attack


class TestEnemyAttack(TestCase):
    @patch("random.randint", return_value=1)
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_enemy_normal_attack(self, mock_output, _):
        character = {"Defence": 2, "Current HP": 10}
        foe = {"Name": "Orc", "Attack": 2}
        enemy_attack(character, foe)
        actual = mock_output.getvalue()
        expected = "The Orc counterattacks and deals 1 damage!\n"
        self.assertEqual(actual, expected)

    @patch("random.randint", return_value=1)
    @patch("random.random", return_value=0.24)
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_enemy_ability_attack(self, mock_output, _, __):
        character = {"Defence": 2, "Current HP": 15}
        foe = {
            "Name": "High Orc",
            "Attack": 7,
            "Current HP": 16,
            "Defence": 2,
            "Ability": {
                "Spear Throw": {"Power": 4, "Description": "The High Orc aims its spear at you!"},
            },
        }
        enemy_attack(character, foe)
        actual = mock_output.getvalue()
        expected = "The High Orc aims its spear at you!\n" \
                   "The High Orc uses Spear Throw and deals 10 damage!\n"
        self.assertEqual(actual, expected)

    @patch("random.randint", return_value=1)
    @patch("random.random", return_value=0.24)
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_enemy_special_ability_attack(self, mock_output, _, __):
        character = {"Defence": 2, "Current HP": 50}
        foe = {
            "Name": "Time Warden",
            "Attack": 15,
            "Max HP": 100,
            "Current HP": 50,
            "Defence": 5,
            "Ability": {
                "Hasten": {"Power": 12, "Description": "The Time Warden hastens itself and attacks rapidly!"},
                "Temporal Shift": {"Power": 15, "Description": "The Time Warden releases time-warping energy!"},
            },
            "Special Ability": {
                "Chrono Stasis": {"Power": 25, "Description": "The Time Warden tries to control your flow of time!"},
            },
            "Special Ability Counter": 0,
        }
        enemy_attack(character, foe)
        actual = mock_output.getvalue()
        expected = "The Time Warden tries to control your flow of time!\n" \
                   "Your Radiant Blade and Guardian Armour are reacting to the Time Warden's special ability!\n" \
                   "You are able to withstand its manipulation of time!\n" \
                   "Your special items mitigate Chrono Stasis and it only deals 39 damage!\n" \
                   "You sense that the Time Warden is nearing defeat.\n"
        self.assertEqual(actual, expected)

    @patch("random.randint", return_value=1)
    @patch("random.choice", return_value="Temporal Shift")
    @patch("random.random", return_value=0.24)
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_enemy_special_ability_attack_already_used(self, mock_output, _, __, ___):
        character = {"Defence": 2, "Current HP": 50}
        foe = {
            "Name": "Time Warden",
            "Attack": 15,
            "Max HP": 100,
            "Current HP": 30,
            "Defence": 5,
            "Ability": {
                "Hasten": {"Power": 12, "Description": "The Time Warden hastens itself and attacks rapidly!"},
                "Temporal Shift": {"Power": 15, "Description": "The Time Warden releases time-warping energy!"},
            },
            "Special Ability": {
                "Chrono Stasis": {"Power": 25, "Description": "The Time Warden tries to control your flow of time!"},
            },
            "Special Ability Counter": 1,
        }
        enemy_attack(character, foe)
        actual = mock_output.getvalue()
        expected = "The Time Warden releases time-warping energy!\n" \
                   "The Time Warden uses Temporal Shift and deals 29 damage!\n"
        self.assertEqual(actual, expected)

    @patch("random.randint", return_value=1)
    @patch("random.choice", return_value="Temporal Shift")
    @patch("random.random", return_value=0.24)
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_player_hp_above_half_special_ability_not_used(self, mock_output, _, __, ___):
        character = {"Defence": 2, "Current HP": 50}
        foe = {
            "Name": "Time Warden",
            "Attack": 15,
            "Max HP": 100,
            "Current HP": 51,
            "Defence": 5,
            "Ability": {
                "Hasten": {"Power": 12, "Description": "The Time Warden hastens itself and attacks rapidly!"},
                "Temporal Shift": {"Power": 15, "Description": "The Time Warden releases time-warping energy!"},
            },
            "Special Ability": {
                "Chrono Stasis": {"Power": 25, "Description": "The Time Warden tries to control your flow of time!"},
            },
            "Special Ability Counter": 0,
        }
        enemy_attack(character, foe)
        actual = mock_output.getvalue()
        expected = "The Time Warden releases time-warping energy!\n" \
                   "The Time Warden uses Temporal Shift and deals 29 damage!\n"
        self.assertEqual(actual, expected)

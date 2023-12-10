"""
Jason Chow
A00942129
"""
import io
from unittest import TestCase
from unittest.mock import patch
from loot import battle_rewards
from utility import draw_box


class TestBattleRewards(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_battle_rewards_cheap_trinket(self, mock_output):
        character = {
            "Inventory": {
                "1": {"Name": "Bronze Sword", "Power": 0, "Type": "Weapon"},
                "2": {"Name": "Clothes", "Power": 0, "Type": "Armour"}
            },
            "Gold": 0,
            "Level": 1,
            "Experience Points": 0,
            "EXP to Level Up": 10,
        }
        foe = {
            "Name": "Goblin",
            "Experience Points": 5,
            "Gold": 5,
            "Loot": {
                "Cheap Trinket": {"Price": 10, "Type": "Miscellaneous"},
            }
        }
        battle_rewards(character, foe)
        actual = mock_output.getvalue()
        expected = "xX------------------------------------------------------Xx\n" \
                   "You defeated the Goblin and earned 5 gold!\n" \
                   "You gained 5 experience points!\n" \
                   "Your total gold is now 5.\n" \
                   "You obtained a sellable miscellaneous item: Cheap Trinket!\n" \
                   "You added 1 Cheap Trinket(s) to your inventory!\n"
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_battle_rewards_frozen_orb(self, mock_output):
        character = {
            "Inventory": {
                "1": {"Name": "Bronze Sword", "Power": 0, "Type": "Weapon"},
                "2": {"Name": "Clothes", "Power": 0, "Type": "Armour"}
            },
            "Gold": 0,
            "Level": 1,
            "Experience Points": 0,
            "EXP to Level Up": 10,
        }
        foe = {
            "Name": "Ice Guardian",
            "Experience Points": 50,
            "Gold": 50,
            "Loot": {
                "Frozen Orb": {"Type": "Special"},
            }
        }
        battle_rewards(character, foe)
        actual = mock_output.getvalue()
        expected = (
                "xX------------------------------------------------------Xx\n"
                "You defeated the Ice Guardian and earned 50 gold!\n"
                "You gained 50 experience points!\n"
                "Your total gold is now 50.\n"
                + draw_box("You obtained a special item: Frozen Orb!") +
                "\n" "You added 1 Frozen Orb(s) to your inventory!\n"
        )
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_battle_rewards_radiant_blade(self, mock_output):
        character = {
            "Attack": 2,
            "Inventory": {
                "1": {"Name": "Bronze Sword", "Power": 0, "Type": "Weapon"},
                "2": {"Name": "Clothes", "Power": 0, "Type": "Armour"}
            },
            "Gold": 0,
            "Level": 1,
            "Experience Points": 0,
            "EXP to Level Up": 10,
        }
        foe = {
            "Name": "Ice Guardian",
            "Experience Points": 50,
            "Gold": 50,
            "Loot": {
                "Radiant Blade": {"Type": "Equipment"},
            }
        }
        battle_rewards(character, foe)
        actual = mock_output.getvalue()
        expected = (
                "xX------------------------------------------------------Xx\n"
                "You defeated the Ice Guardian and earned 50 gold!\n"
                "You gained 50 experience points!\n"
                "Your total gold is now 50.\n"
                + draw_box("You obtained a special weapon: Radiant Blade!") +
                "\n" "Replacing Bronze Sword with Radiant Blade in your inventory.\n"
        )
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_battle_rewards_guardian_armour(self, mock_output):
        character = {
            "Defence": 2,
            "Inventory": {
                "1": {"Name": "Bronze Sword", "Power": 0, "Type": "Weapon"},
                "2": {"Name": "Clothes", "Power": 0, "Type": "Armour"}
            },
            "Gold": 0,
            "Level": 1,
            "Experience Points": 0,
            "EXP to Level Up": 10,
        }
        foe = {
            "Name": "Ice Guardian",
            "Experience Points": 50,
            "Gold": 50,
            "Loot": {
                "Guardian Armour": {"Type": "Equipment"},
            }
        }
        battle_rewards(character, foe)
        actual = mock_output.getvalue()
        expected = (
                "xX------------------------------------------------------Xx\n"
                "You defeated the Ice Guardian and earned 50 gold!\n"
                "You gained 50 experience points!\n"
                "Your total gold is now 50.\n"
                + draw_box("You obtained special armor: Guardian Armour!") +
                "\n" "Replacing Clothes with Guardian Armour in your inventory.\n"
        )
        self.assertEqual(actual, expected)

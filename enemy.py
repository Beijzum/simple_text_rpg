import random
from unittest.mock import patch


def check_for_foes():
    """
    Check for foes at a rate of 1 in 4 (25%).

    :param: N/A
    :precondition: character must be alive with greater than 0 HP
    :postcondition: checks for the probability of encountering a challenge
    :return: returns True at a rate of 25%, otherwise False at a rate of 75%
    >>> with patch('random.random', return_value=0.1):
    ...     check_for_foes()
    Watch out! Something has seen you!
    True
    >>> with patch('random.random', return_value=0.5):
    ...     check_for_foes()
    You managed to avoid enemies.
    False
    """
    if random.random() <= 0.25:
        print("Watch out! Something has seen you!")
        return True

    else:
        print("You managed to avoid enemies.")
        return False


def generate_foe():
    """
    Generate a random foe from a list of possible foes.

    :param: N/A
    :precondition: character must be alive with greater than 0 HP
    :postcondition: generates a random foe from a list of possible foes
    :return: returns a dictionary containing the foe's stats

    >>> with patch('random.choice', return_value='Goblin'):
    ...     generate_foe()
    {'Name': 'Goblin', 'Attack': 1, 'Current HP': 3, 'Defence': 0, 'Gold': 5, 'Experience Points': 5,\
 'Loot': {'Cheap Trinket': {'Price': 8, 'Type': 'Miscellaneous'}}}

    >>> with patch('random.choice', return_value='Orc'):
    ...     generate_foe()
    {'Name': 'Orc', 'Attack': 2, 'Current HP': 6, 'Defence': 1, 'Gold': 10, 'Experience Points': 10,\
 'Loot': {'Cheap Trinket': {'Price': 8, 'Type': 'Miscellaneous'}}}
    """
    foe_types = ["Goblin", "Orc", "Skeleton", "Ghoul"]
    random_foe = random.choice(foe_types)

    if random_foe == "Goblin":
        return {
            "Name": "Goblin",
            "Attack": 1,
            "Current HP": 3,
            "Defence": 0,
            "Gold": 5,
            "Experience Points": 5,
            "Loot": {
                "Cheap Trinket": {"Price": 8, "Type": "Miscellaneous"},
            }
        }
    elif random_foe == "Orc":
        return {
            "Name": "Orc",
            "Attack": 2,
            "Current HP": 6,
            "Defence": 1,
            "Gold": 10,
            "Experience Points": 10,
            "Loot": {
                "Cheap Trinket": {"Price": 8, "Type": "Miscellaneous"},
            }
        }
    elif random_foe == "Skeleton":
        return {
            "Name": "Skeleton",
            "Attack": 2,
            "Current HP": 3,
            "Defence": 1,
            "Gold": 5,
            "Experience Points": 5,
            "Loot": {
                "Cheap Trinket": {"Price": 8, "Type": "Miscellaneous"},
            }
        }
    elif random_foe == "Ghoul":
        return {
            "Name": "Ghoul",
            "Attack": 1,
            "Current HP": 8,
            "Defence": 0,
            "Gold": 5,
            "Experience Points": 10,
            "Loot": {
                "Cheap Trinket": {"Price": 8, "Type": "Miscellaneous"},
            }
        }


def generate_stronger_foe():
    """
    Generate a random stronger foe from a list of possible foes.

    After an event, there will be a 1 in 4 chance of encountering a stronger foe.

    :param: N/A
    :precondition: character must be alive with greater than 0 HP
    :precondition: character must have Frozen Orb and Flame Orb in inventory
    :postcondition: generates a random stronger foe from a list of possible foes
    :return: returns a dictionary containing the stronger foe's stats

    >>> with patch('random.choice', return_value='Hobgoblin'):
    ...     generate_stronger_foe()
    {'Name': 'Hobgoblin', 'Attack': 5, 'Current HP': 8, 'Defence': 1, 'Ability': {'Reckless Attack': {'Power': 2,\
 'Description': 'The Hobgoblin is charging at you!'}}, 'Gold': 10, 'Experience Points': 10,\
 'Loot': {'Rare Relic': {'Price': 16, 'Type': 'Miscellaneous'}}}

    >>> with patch('random.choice', return_value='High Orc'):
    ...     generate_stronger_foe()
    {'Name': 'High Orc', 'Attack': 7, 'Current HP': 16, 'Defence': 2, 'Ability': {'Spear Throw': {'Power': 4,\
 'Description': 'The High Orc aims its spear at you!'}}, 'Gold': 20, 'Experience Points': 20,\
 'Loot': {'Rare Relic': {'Price': 16, 'Type': 'Miscellaneous'}}}
    """
    foe_types = ["Hobgoblin", "High Orc", "Iron-Clad Skeleton", "Draugr", "Wyvern"]
    random_foe = random.choice(foe_types)

    if random_foe == "Hobgoblin":
        return {
            "Name": "Hobgoblin",
            "Attack": 5,
            "Current HP": 8,
            "Defence": 1,
            "Ability": {
                "Reckless Attack": {"Power": 2, "Description": "The Hobgoblin is charging at you!"},
            },
            "Gold": 10,
            "Experience Points": 10,
            "Loot": {
                "Rare Relic": {"Price": 16, "Type": "Miscellaneous"},
            }
        }
    elif random_foe == "High Orc":
        return {
            "Name": "High Orc",
            "Attack": 7,
            "Current HP": 16,
            "Defence": 2,
            "Ability": {
                "Spear Throw": {"Power": 4, "Description": "The High Orc aims its spear at you!"},
            },
            "Gold": 20,
            "Experience Points": 20,
            "Loot": {
                "Rare Relic": {"Price": 16, "Type": "Miscellaneous"},
            }
        }
    elif random_foe == "Iron-Clad Skeleton":
        return {
            "Name": "Iron-Clad Skeleton",
            "Attack": 6,
            "Current HP": 10,
            "Defence": 5,
            "Ability": {
                "Downward Smash": {"Power": 3, "Description": "The Iron-Clad Skeleton raises its weapon!"},
            },
            "Gold": 10,
            "Experience Points": 20,
            "Loot": {
                "Rare Relic": {"Price": 16, "Type": "Miscellaneous"},
            }
        }
    elif random_foe == "Draugr":
        return {
            "Name": "Draugr",
            "Attack": 5,
            "Current HP": 23,
            "Defence": 1,
            "Ability": {
                "Deadly Bite": {"Power": 4, "Description": "The Draugr lunges at you!"},
            },
            "Gold": 10,
            "Experience Points": 20,
            "Loot": {
                "Rare Relic": {"Price": 16, "Type": "Miscellaneous"},
            }
        }
    elif random_foe == "Wyvern":
        return {
            "Name": "Wyvern",
            "Attack": 9,
            "Current HP": 30,
            "Defence": 3,
            "Ability": {
                "Wyvern's Breath": {"Power": 6, "Description": "The Wvyern reveals its wide maw!"},
            },
            "Gold": 20,
            "Experience Points": 30,
            "Loot": {
                "Rare Relic": {"Price": 16, "Type": "Miscellaneous"},
            }
        }


def generate_special_foe(board, character):
    """
    Generate a special foe based on the character's current location on the board.

    :param board: a dictionary with the board's layout and coordinates
    :param character: a dictionary with character stats
    :precondition: character must be alive with greater than 0 HP
    :precondition: character must be in a special room
    :precondition: depending on the foe, character must have Frozen Orb and Flame Orb in inventory
    :precondition: depending on the foe, character must have Radiant Blade and Guardian Armour in inventory
    :postcondition: generates a special foe based on the character's current location on the board and inventory
    :return: a dictionary representing the generated foe.

    >>> test_board = {(0, 0): "Winter Sanctum"}
    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> generate_special_foe(test_board, test_character)
    {'Name': 'Abominable Snowman', 'Attack': 4, 'Current HP': 30, 'Defence': 2, 'Ability': {\
'Snowball': {'Power': 4, 'Description': 'The Abominable Snowman throws a giant snowball at you!'}}, \
'Gold': 30, 'Experience Points': 30, 'Loot': {'Frozen Orb': {'Type': 'Special'}}}

    >>> test_board = {(0, 0): "Inferno Lair"}
    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> generate_special_foe(test_board, test_character)
    {'Name': 'Dragon', 'Attack': 6, 'Current HP': 50, 'Defence': 3, 'Ability': {\
'Flame Breath': {'Power': 4, 'Description': 'The Dragon unleashes a fiery breath!'}}, \
'Gold': 40, 'Experience Points': 40, 'Loot': {'Flame Orb': {'Type': 'Special'}}}
    """
    x = character["X-coordinate"]
    y = character["Y-coordinate"]
    coordinate = (x, y)

    if board.get(coordinate) == "Winter Sanctum":
        return {
            "Name": "Abominable Snowman",
            "Attack": 4,
            "Current HP": 30,
            "Defence": 2,
            "Ability": {
                "Snowball": {"Power": 4, "Description": "The Abominable Snowman throws a giant snowball at you!"},
            },
            "Gold": 30,
            "Experience Points": 30,
            "Loot": {
                "Frozen Orb": {"Type": "Special"},
            }

        }
    elif board.get(coordinate) == "Inferno Lair":
        return {
            "Name": "Dragon",
            "Attack": 6,
            "Current HP": 50,
            "Defence": 3,
            "Ability": {
                "Flame Breath": {"Power": 4, "Description": "The Dragon unleashes a fiery breath!"},
            },
            "Gold": 40,
            "Experience Points": 40,
            "Loot": {
                "Flame Orb": {"Type": "Special"},
            }
        }
    elif board.get(coordinate) == "Ice Guardian Room":
        return {
            "Name": "Ice Guardian",
            "Attack": 12,
            "Current HP": 80,
            "Defence": 4,
            "Ability": {
                "Snowstorm": {"Power": 8, "Description": "The Ice Guardian is creating a snowstorm!"},
                "Frostbite": {"Power": 10, "Description": "The Ice Guardian is rapidly lowering the temperature!"},
            },
            "Gold": 100,
            "Experience Points": 50,
            "Loot": {
                "Guardian Armour": {"Type": "Equipment"},
            }
        }
    elif board.get(coordinate) == "Fire Guardian Room":
        return {
            "Name": "Fire Guardian",
            "Attack": 12,
            "Current HP": 80,
            "Defence": 4,
            "Ability": {
                "Infernal Blaze": {"Power": 8, "Description": "The Fire Guardian conjures fiery devastation!"},
                "Scorching Heat": {"Power": 10, "Description": "The Fire Guardian is raising the temperature!"},
            },
            "Gold": 100,
            "Experience Points": 50,
            "Loot": {
                "Radiant Blade": {"Type": "Equipment"},
            }
        }
    elif board.get(coordinate) == "Final Room":
        return {
            "Name": "Time Warden",
            "Attack": 15,
            "Max HP": 100,
            "Current HP": 100,
            "Defence": 5,
            "Ability": {
                "Hasten": {"Power": 12, "Description": "The Time Warden hastens itself and attacks rapidly!"},
                "Temporal Shift": {"Power": 15, "Description": "The Time Warden releases time-warping energy!"},
            },
            "Special Ability": {
                "Chrono Stasis": {"Power": 25, "Description": "The Time Warden tries to control your flow of time!"},
            },
            "Special Ability Counter": 0,
            "Gold": 1000,
            "Experience Points": 1000,
            "Loot": {
                "Orb of Time": {"Type": "Special"},
            }
        }

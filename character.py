def make_character():
    """
    Create a character when invoking this function.

    :param: N/A
    :precondition: a dictionary with x, y coordinates, and HP counter
    :postcondition: creates a character with the given starting location, HP, Attack, and Defence
    :return: a dictionary with coordinates at 0, 0, 5 HP, 1 Attack, and 0 Defence

#     >>> make_character()
#     {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10, 'Attack': 1, 'Defence': 0, 'Inventory': [], \
# 'Level': 1, 'Experience Points': 0, 'EXP to Level Up': 10}
    """
    return {
        "X-coordinate": 0,
        "Y-coordinate": 0,
        "Max HP": 10,
        "Current HP": 10,
        "Max AP": 5,
        "Ability Points": 5,
        "Attack": 1,
        "Defence": 0,
        "Abilities": {
            "1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1},
        },
        "Inventory": {
            "1": {"Name": "Bronze Sword", "Power": 0, "Type": "Weapon"},
            "2": {"Name": "Clothes", "Power": 0, "Type": "Armour"},
        },
        "Gold": 0,
        "Level": 1,
        "Experience Points": 0,
        "EXP to Level Up": 10,
        "Stronger Enemies": False,
    }


def get_character_stats(character):
    """
    """
    print(f"Your current Level is {character['Level']}.")
    print(f"Your current Max HP is {character['Max HP']}.")
    print(f"Your current HP is {character['Current HP']}.")
    print(f"Your current Max AP is {character['Max AP']}.")
    print(f"Your current Ability Points is {character['Ability Points']}.")
    print(f"Your current Attack is {character['Attack']}.")
    print(f"Your current Defence is {character['Defence']}.")
    print(f"Your current Abilities are {character['Abilities']}.")
    print(f"Your current Experience Points is {character['Experience Points']}.")
    print(f"Your current EXP to Level Up is {character['EXP to Level Up']}.")
    print(f"Your current Gold is {character['Gold']}.")
    print(f"Your current coordinates are ({character['X-coordinate']},{character['Y-coordinate']}).")


def get_character_inventory(character):
    """
    """
    for key, value in character['Inventory'].items():
        print(f"Item #{key} {value}.")


def level_up(character):
    """
    """
    character["Max HP"] += 5
    character["Current HP"] = character["Max HP"]  # Player recovers full HP
    character["Max AP"] += 2
    character["Ability Points"] = character["Max AP"]  # Player recovers full AP
    character["Attack"] += 1
    character["Defence"] += 1
    character["Level"] += 1
    character['Experience Points'] -= character['EXP to Level Up']
    character['EXP to Level Up'] = int(character['EXP to Level Up'] * 1.5)
    print(f"Congratulations! You leveled up to Level {character['Level']}!")
    print(f"Your Max HP is now {character['Max HP']}.")
    print(f"Your Max AP is now {character['Max AP']}.")
    print(f"Your Attack is now {character['Attack']}.")
    print(f"Your Defence is now {character['Defence']}.")

    learn_ability(character)

    return character


def learn_ability(character):
    if character['Level'] == 3:
        ability_count = len(character['Abilities']) + 1
        new_ability = {"Name": "Multi-Strike", "Power": 2, "AP Cost": 2}
        character['Abilities'][str(ability_count)] = new_ability
        print(f"You learned a new ability: {new_ability['Name']}!")

    elif character['Level'] == 5:
        ability_count = len(character['Abilities']) + 1
        new_ability = {"Name": "Holy Strike", "Power": 7, "AP Cost": 3}
        character['Abilities'][str(ability_count)] = new_ability
        print(f"You learned a new ability: {new_ability['Name']}!")

    elif character['Level'] == 7:
        ability_count = len(character['Abilities']) + 1
        new_ability = {"Name": "Ultimate Strike", "Power": 10, "AP Cost": 5}
        character['Abilities'][str(ability_count)] = new_ability
        print(f"You learned a new ability: {new_ability['Name']}!")

    elif character['Level'] == 10:
        ability_count = len(character['Abilities']) + 1
        new_ability = {"Name": "You're Playing Too Long", "Power": 999, "AP Cost": 10}
        character['Abilities'][str(ability_count)] = new_ability
        print(f"You learned a new ability: {new_ability['Name']}!")


def is_alive(character):
    """
    Check if the character is alive with greater than 0 health.

    :param character: a non-empty dictionary
    :precondition: character must be a dictionary with x, y coordinates, and HP counter
    :postcondition: checks if the character has greater than 0 HP
    :return: returns True if character has more than 0 HP, otherwise False if character HP is 0

    >>> character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> is_alive(character_test)
    True

    >>> character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 0}
    >>> is_alive(character_test)
    False
    """
    return True if character['Current HP'] > 0 else False

def make_character():
    """
    Create a character when invoking this function.

    :param: N/A
    :precondition: user must start a new game
    :postcondition: creates a character with the given starting location, stats, inventory, and event checks
    :return: a dictionary representing the player character with coordinates, stats, inventory, and event checks

    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Max HP': 10, 'Current HP': 10, 'Max AP': 5, 'Ability Points': 5,\
 'Attack': 2, 'Defence': 0, 'Abilities': {'1': {'Name': 'Power Strike', 'Power': 2, 'AP Cost': 1}},\
 'Inventory': {'1': {'Name': 'Bronze Sword', 'Power': 0, 'Type': 'Weapon'}, '2': {'Name': 'Clothes',\
 'Power': 0, 'Type': 'Armour'}}, 'Gold': 0, 'Level': 1, 'Experience Points': 0, 'EXP to Level Up': 10,\
 'Stronger Enemies': False}
    """
    return {
        "X-coordinate": 0,
        "Y-coordinate": 0,
        "Max HP": 10,
        "Current HP": 10,
        "Max AP": 5,
        "Ability Points": 5,
        "Attack": 2,
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
    Print the current stats of the character.

    :param character: a dictionary representing the player character
    :precondition: character must be alive with greater than 0 health.
    :precondition: character must have stats in the form of a dictionary.
    :postcondition: prints the current stats of the character to the console.
    :return: a string of the current stats of the character.

    >>> character_test = {"Level": 1, "Max HP": 10, "Current HP": 10, "Max AP": 5, "Ability Points": 5, "Attack": 1,\
 "Defence": 0, "Abilities": {"1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1}}, "Experience Points": 0,\
 "EXP to Level Up": 10, "Gold": 0, "X-coordinate": 0, "Y-coordinate": 0}
    >>> get_character_stats(character_test)
    Your current Level is 1.
    Your current Max HP is 10.
    Your current HP is 10.
    Your current Max AP is 5.
    Your current Ability Points is 5.
    Your current Attack is 1.
    Your current Defence is 0.
    Your current Abilities are {'1': {'Name': 'Power Strike', 'Power': 2, 'AP Cost': 1}}.
    Your current Experience Points is 0.
    Your current EXP to Level Up is 10.
    Your current Gold is 0.
    Your current coordinates are (0,0).
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
    Print the current inventory of the character.

    :param character: a dictionary representing the player character
    :precondition: character must be alive with greater than 0 health.
    :precondition: character must have an inventory in the form of a dictionary.
    :postcondition: prints the current inventory of the character to the console.
    :return: a string of the current inventory of the character.

    >>> character_test = {"Inventory": {"1": {"Name": "Bronze Sword", "Power": 0, "Type": "Weapon"},\
 "2": {"Name": "Clothes", "Power": 0, "Type": "Armour"}}}
    >>> get_character_inventory(character_test)
    Item #1 {'Name': 'Bronze Sword', 'Power': 0, 'Type': 'Weapon'}.
    Item #2 {'Name': 'Clothes', 'Power': 0, 'Type': 'Armour'}.
    """
    for key, value in character['Inventory'].items():
        print(f"Item #{key} {value}.")


def level_up(character):
    """
    Level up the character, increasing their stats and learning new abilities if applicable.

    :param character: a dictionary representing the player character
    :precondition: character must be alive with greater than 0 health.
    :precondition: character must be a dictionary with stats and abilities
    :postcondition: updates the character's stats
    :postcondition: prints the new character stats
    :postcondition: learns new abilities if applicable
    :return: a dictionary representing the updated player character
    :return: strings representating the increased stats of the character

    >>> character_test = {"Max HP": 10, "Current HP": 10, "Max AP": 5, "Ability Points": 5,\
 "Attack": 1, "Defence": 0, "Level": 1, "Experience Points": 10, "EXP to Level Up": 10}
    >>> level_up(character_test)
    Congratulations! You leveled up to Level 2!
    Your Max HP is now 15.
    Your Max AP is now 7.
    Your Attack is now 2.
    Your Defence is now 1.
    {'Max HP': 15, 'Current HP': 15, 'Max AP': 7, 'Ability Points': 7, 'Attack': 2, 'Defence': 1, 'Level': 2,\
 'Experience Points': 0, 'EXP to Level Up': 15}
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
    """
    Learn a new ability when the character levels up.

    :param character: a dictionary representing the player character
    :precondition: character must be alive with greater than 0 health.
    :precondition: character must be a dictionary with 'Level' and 'Abilities' keys
    :postcondition: updates the character's abilities based on their level
    :postcondition: prints the new ability learned
    :return: a string representing the new ability learned
    :return: a dictionary representing the updated player character

    >>> character_test = {"Level": 3, "Abilities": {"1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1},\
 "2": {"Name": "Multi-Strike", "Power": 2, "AP Cost": 2}}}
    >>> learn_ability(character_test)
    You learned a new ability: Multi-Strike!

    >>> character_test = {"Level": 5, "Abilities": {"1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1},\
 "2": {"Name": "Multi-Strike", "Power": 2, "AP Cost": 2}, "3": {"Name": "Holy Strike", "Power": 7, "AP Cost": 3}}}
    >>> learn_ability(character_test)
    You learned a new ability: Holy Strike!
    """
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
    Check if the character (or foe) is alive with greater than 0 health.

    :param character: a non-empty dictionary
    :precondition: character must be a dictionary with the key "Current HP"
    :postcondition: checks if the character has greater than 0 HP
    :return: returns True if current HP is more than 0, otherwise False if current HP is not greater than 0

    >>> character_test = {"Current HP": 5}
    >>> is_alive(character_test)
    True

    >>> character_test = {"Current HP": 0}
    >>> is_alive(character_test)
    False
    """
    return True if character['Current HP'] > 0 else False

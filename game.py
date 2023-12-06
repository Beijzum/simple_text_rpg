"""
Jason Chow
A00942129
"""
import random
import json
import sys
import os


def clear():
    """
    Clear the terminal screen for better readability.

    This function will use "cls" for a Windows OS, else it will use "clear".
    """
    os.system("cls" if os.name == "nt" else "clear")


def start_menu():
    """
    Display the start menu with a choice of starting a new game, loading a game, or quitting.
    """
    print("The Quest For The Chocolate Orb!")
    print("1. Start a New Game")
    print("2. Load Game")
    print("3. Quit")

    while True:
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            clear()
            game()
            break
        elif choice == "2":
            clear()
            load_game()
            break
        elif choice == "3":
            print("Goodbye! Thanks for playing.")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def save_game(character):
    """
    Save the current game state to a JSON file.
    """
    with open("save.json", "w") as game_file:
        json.dump(character, game_file, indent=4)

    print("Game saved successfully!")


def load_game():
    """
    Load an existing game and continue.
    """
    try:
        with open("save.json", "r") as game_file:
            character = json.load(game_file)

        print("Game loaded successfully!")
        game(character)

    except FileNotFoundError:
        print("No saved game found.")
        start_menu()


def make_board(rows, columns):
    """
    Create a board to represent the playable area.

    :param rows: an integer
    :param columns: an integer
    :precondition: rows must be an integer >= 2
    :precondition: columns must be an integer >= 2
    :postcondition: creates a dictionary based on the rows and columns values
    :postcondition: rooms will be randomly populated
    :return: a dictionary with x, y coordinates as a key, and a room name as a value
    """
    board = {}
    room_list = ["Treasure Room", "Enchanted Chamber", "Empty Room", "Dark Room"]

    for row in range(rows):
        for column in range(columns):

            if (row, column) == (0, 0):
                board[(row, column)] = "Starting Room"

            elif (row, column) == (rows - 1, columns - 1):
                board[(row, column)] = "Final Room"

            elif (row, column) == (rows - 1, 0):
                board[(row, column)] = "Inferno Lair"

            elif (row, column) == (rows - 1, columns - 2):
                board[(row, column)] = "Fire Guardian Room"

            elif (row, column) == (0, columns - 1):
                board[(row, column)] = "Winter Sanctum"

            elif (row, column) == (rows - 2, columns - 1):
                board[(row, column)] = "Ice Guardian Room"

            elif (row, column) == (int(rows / 2), int(columns / 2)):
                board[(row, column)] = "Traveling Merchant"

            else:
                room = random.choice(room_list)
                board[(row, column)] = room

    return board


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
        "Gold": 100,
        "Level": 1,
        "Experience Points": 0,
        "EXP to Level Up": 10
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


def show_map(board_rows, board_columns, character):
    rows = board_rows
    columns = board_columns

    player_location = character["X-coordinate"], character["Y-coordinate"]

    for row in range(rows):
        print("----------------------------------------------")
        for column in range(columns):
            position = (row, column)
            if position == player_location:
                print("| @Player", end="")
            elif position == (int(rows / 2), int(columns / 2)):
                print("| $Shop ", end=" ")
            elif position in [(rows - 1, 0), (0, columns - 1), (rows - 1, columns - 2), (rows - 2, columns - 1)]:
                print("|#Special", end="")
            elif position == (rows - 1, columns - 1):
                print("| #Boss ", end=" ")
            else:
                print(f"| ({row}, {column})", end=" ")

        print("|")
    print("----------------------------------------------")


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
        new_ability = {"Name": "Multi-Strike", "Power": 4, "AP Cost": 2}
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


def describe_current_location(board, character):
    """
    Print the current location of the player character.

    :param board: a non-empty dictionary
    :param character: a non-empty dictionary
    :precondition: character must be alive with greater than 0 HP
    :precondition: board must be a dictionary with x, y coordinates as a key, and a room name as a value
    :precondition: character must be a dictionary with x, y coordinates, and HP counter
    :postcondition: assigns player_location variable as character coordinates from the character dictionary
    :return: prints the room name and x and y coordinates

    >>> describe_current_location({(2, 0): "Dark Room"}, {'X-coordinate': 2, 'Y-coordinate': 0, 'Current HP': 5})
    Dark Room (2, 0)
    You see nothing but darkness in this room.
    >>> describe_current_location({(1, 1): "Empty Room"}, {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5})
    Empty Room (1, 1)
    You see nothing interesting in this room.
    """
    player_location = character["X-coordinate"], character["Y-coordinate"]
    print(board[player_location], player_location)
    if board[player_location] == "Starting Room":
        print("This is the beginning of your adventure.")
    elif board[player_location] == "Treasure Room":
        print("You see lots of treasure in this room.")
    elif board[player_location] == "Enchanted Chamber":
        print("You feel magic everywhere in this chamber.")
    elif board[player_location] == "Empty Room":
        print("You see nothing interesting in this room.")
    elif board[player_location] == "Dark Room":
        print("You see nothing but darkness in this room.")
    elif board[player_location] == "Traveling Merchant":
        print("You see a merchant selling wares.")
    elif board[player_location] == "Inferno Lair":
        print("You sense the warmth emanating from the scorching depths of molten rage and foreboding radiance.")
    elif board[player_location] == "Fire Guardian Room":
        print("You see a fiery sentinel standing watch over an orb pedestal.")
    elif board[player_location] == "Winter Sanctum":
        print("You feel the frigid embrace of winter, adorned with shimmering ice formations.")
    elif board[player_location] == "Ice Guardian Room":
        print("You see an icy sentinel standing watch over an orb pedestal.")
    elif (board[player_location] == "Final Room" and
          not any(item['Name'] == "Radiant Blade" for item in character['Inventory'].values()) or
          not any(item['Name'] == "Guardian Armour" for item in character['Inventory'].values())):
        print("You see a large, menacing creature guarding the room.")
        print("You must find the two special items to defeat this foe.")


def get_user_choice(rows, columns, character):
    """
    Prompt user for input to choose a direction from a numbered list.

    :param: N/A
    :precondition: user must input a number between 1 and 4
    :precondition: character must be alive with greater than 0 HP
    :precondition: character must not be in the winning room
    :postcondition: prompts user to choose a direction and returns the input as a string
    :return: returns a string consisting of "up", "down", "left", or "right"
    """
    while True:
        print("1. Up")
        print("2. Down")
        print("3. Left")
        print("4. Right")
        user_input = input("Please choose a direction (1, 2, 3, or 4) or show map(5), character stats(6), "
                           "inventory(7), save game(8), start menu(0): ")

        if user_input == "1":
            print("You chose to go up...")
            return "up"

        elif user_input == "2":
            print("You chose to go down...")
            return "down"

        elif user_input == "3":
            print("You chose to go left...")
            return "left"

        elif user_input == "4":
            print("You chose to go right...")
            return "right"

        elif user_input == "5":
            clear()
            show_map(rows, columns, character)

        elif user_input == "6":
            clear()
            get_character_stats(character)

        elif user_input == "7":
            clear()
            get_character_inventory(character)

        elif user_input == "8":
            clear()
            save_game(character)

        elif user_input == "0":
            clear()
            start_menu()

        else:
            print("Invalid choice.")


def validate_move(board, character, direction):
    """
    Validate the user's input and assures that the direction is not out of bounds of the board.

    :param board: a non-empty dictionary
    :param character: a non-empty dictionary
    :param direction: a string
    :precondition: character must be alive with greater than 0 HP
    :precondition: board must be a dictionary with x, y coordinates as a key, and a room name as a value
    :precondition: character must be a dictionary with x, y coordinates, and HP counter
    :precondition: a string containing "up", "down", "left", or "right"
    :postcondition: determines if the direction is out of bounds of the board
    :return: returns True if the direction is valid, otherwise False

    # Variables
    >>> board_test = {(0, 0): "Starting Room", (0, 1): "Empty Room", (1, 0): "Empty Room"}
    >>> character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}

    >>> validate_move(board_test, character_test, "down")
    True

    >>> validate_move(board_test, character_test, "left")
    False
    """
    x = character["X-coordinate"]
    y = character["Y-coordinate"]

    if direction == "up":
        x -= 1
    elif direction == "down":
        x += 1
    elif direction == "left":
        y -= 1
    elif direction == "right":
        y += 1

    coordinates = (x, y)

    if coordinates not in board:
        return False
    else:
        return True


def move_character(character, direction):
    """
    Move a character on the board in one of four directions.

    :param character: a non-empty dictionary
    :param direction: a string
    :precondition: character must be alive with greater than 0 HP
    :precondition: direction must be validated by validate_direction function
    :precondition: character must be a dictionary with x, y coordinates, and HP counter
    :precondition: a string containing "up", "down", "left", or "right"
    :precondition: character must not be in the winning room
    :postcondition: moves the player character in a valid direction
    :return: returns a dictionary with updated x, y coordinates depending on the direction

    >>> character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> move_character(character_test, "down")
    {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}

    >>> character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> move_character(character_test, "right")
    {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
    """
    x = character["X-coordinate"]
    y = character["Y-coordinate"]

    if direction == "up":
        x -= 1
    elif direction == "down":
        x += 1
    elif direction == "left":
        y -= 1
    elif direction == "right":
        y += 1

    character["X-coordinate"] = x
    character["Y-coordinate"] = y

    return character


def check_for_foes():
    """
    Check for foes at a rate of 1 in 4 (25%).

    :param: N/A
    :precondition: character must be alive with greater than 0 HP
    :postcondition: checks for the probability of encountering a challenge
    :return: returns True at a rate of 25%, otherwise False at a rate of 75%
    """
    if random.random() <= 0.25:
        print("Watch out! Something has seen you!")
        return True

    else:
        print("You managed to avoid enemies.")
        return False


def generate_foe():
    foe_types = ["Goblin", "Orc", "Skeleton", "Ghoul"]
    random_foe = random.choice(foe_types)

    if random_foe == "Goblin":
        return {
            "Name": "Goblin",
            "Attack": 1,
            "Current HP": 3,
            "Defence": 0,
            "Gold": 10,
            "Experience Points": 5,
        }
    elif random_foe == "Orc":
        return {
            "Name": "Orc",
            "Attack": 2,
            "Current HP": 6,
            "Defence": 1,
            "Gold": 25,
            "Experience Points": 20,
        }
    elif random_foe == "Skeleton":
        return {
            "Name": "Skeleton",
            "Attack": 2,
            "Current HP": 3,
            "Defence": 1,
            "Gold": 15,
            "Experience Points": 10,
        }
    elif random_foe == "Ghoul":
        return {
            "Name": "Ghoul",
            "Attack": 1,
            "Current HP": 8,
            "Defence": 0,
            "Gold": 15,
            "Experience Points": 15,
        }


def generate_special_foe(board, character):
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
            "Gold": 50,
            "Experience Points": 50,
            "Special Item": "Frozen Orb",

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
            "Gold": 100,
            "Experience Points": 50,
            "Special Item": "Flame Orb",
        }
    elif board.get(coordinate) == "Ice Guardian Room":
        return {
            "Name": "Ice Guardian",
            "Attack": 8,
            "Current HP": 70,
            "Defence": 4,
            "Ability": {
                "Snowstorm": {"Power": 6, "Description": "The Ice Guardian is creating a snowstorm!"}
            },
            "Gold": 100,
            "Experience Points": 50,
            "Equipment Item": "Guardian Armour",
        }
    elif board.get(coordinate) == "Fire Guardian Room":
        return {
            "Name": "Fire Guardian",
            "Attack": 8,
            "Current HP": 70,
            "Defence": 4,
            "Ability": {
                "Infernal Blaze": {"Power": 6, "Description": "The Fire Guardian conjures fiery devastation!"}
            },
            "Gold": 100,
            "Experience Points": 50,
            "Equipment Item": "Radiant Blade",
        }
    elif board.get(coordinate) == "Final Room":
        return {
            "Name": "Brain Devourer",
            "Attack": 10,
            "Max HP": 80,
            "Current HP": 80,
            "Defence": 5,
            "Ability": {
                "Ethereal Blast": {"Power": 8, "Description": "A mystic force surges through the fabric of reality!"}
            },
            "Special Ability": {
                "Supernova": {"Power": 25, "Description": "The Brain Devourer is channeling cosmic energy!"},
            },
            "Special Ability Counter": 0,
            "Gold": 1000,
            "Experience Points": 1000,
            "Special Item": "Chocolate Orb",
        }


def check_win_condition(board, character):
    """
    Check if user has reached the goal.

    :param board: a non-empty dictionary
    :param character: a non-empty dictionary
    :precondition: board must be a dictionary with x, y coordinates as a key, and a room name as a value
    :precondition: character must be a dictionary with x, y coordinates, and HP counter
    :precondition: character must be alive with greater than 0 HP
    :postcondition: checks if the user has reached the 'Final Room'
    :return: returns True if player character is located at the 'Final Room', otherwise False

    >>> board_test = {(0, 0): "Starting Room", (2, 2): "Final Room"}
    >>> character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> check_win_condition(board_test, character_test)
    False

    >>> board_test = {(0, 0): "Starting Room", (2, 2): "Final Room"}
    >>> character_test = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 5}
    >>> check_win_condition(board_test, character_test)
    True
    """
    x = character["X-coordinate"]
    y = character["Y-coordinate"]
    coordinate = (x, y)

    if (board.get(coordinate) == "Final Room"
            and any(item['Name'] == "Chocolate Orb" for item in character['Inventory'].values())):
        return True
    else:
        return False


def visit_shop(character):
    """
    """
    print("Welcome to the Shop!")

    while True:
        print("1. Buy Weapon")
        print("2. Buy Armour")
        print("3. Buy Potions")
        print("4. Leave Shop")
        print(f"You currently have {character['Gold']} gold.")
        choice = input("Choose an option (1, 2, 3, or 4): ")

        if choice == "1":  # Buying a weapon
            clear()
            print(f"1. Iron Sword $10\n2. Steel Sword $30")
            weapon_choice = input("Enter the number of the weapon you want to buy: ")

            if weapon_choice == "1":
                weapon_cost = 15
                weapon_name = "Iron Sword"
                weapon_power = 2

            elif weapon_choice == "2":
                weapon_cost = 30
                weapon_name = "Steel Sword"
                weapon_power = 4

            else:
                clear()
                print("Invalid choice. Please enter a valid option.")
                continue

            if character['Gold'] < weapon_cost:
                clear()
                print("Not enough gold to buy the weapon.")

            elif any(item.get('Name') == weapon_name for item in character['Inventory'].values()):
                clear()
                print(f"You already have {weapon_name} in your inventory.")
                continue

            elif any(value['Power'] >= weapon_power for value in character['Inventory'].values() if
                     value['Type'] == 'Weapon'):
                clear()
                print("\"You already have a powerful weapon!\"")
                continue

            else:
                clear()
                print(f"You bought {weapon_name}!")
                character['Gold'] -= weapon_cost
                add_equipment(character, weapon_name, weapon_power, "Weapon")

        elif choice == "2":  # Buying armour
            clear()
            print(f"1. Leather Armour $10\n2. Iron Armour $30")
            armour_choice = input("Enter the number of the armour you want to buy: ")

            if armour_choice == "1":
                armour_cost = 15
                armour_name = "Leather Armour"
                armour_power = 1

            elif armour_choice == "2":
                armour_cost = 30
                armour_name = "Iron Armour"
                armour_power = 2

            else:
                clear()
                print("Invalid choice. Please enter a valid option.")
                continue

            if character['Gold'] < armour_cost:
                clear()
                print("Not enough gold to buy the armour.")

            elif any(item.get('Name') == armour_name for item in character['Inventory'].values()):
                clear()
                print(f"You already have {armour_name} in your inventory.")
                continue

            elif any(value['Power'] >= armour_power for value in character['Inventory'].values() if
                     value['Type'] == 'Armour'):
                clear()
                print("\"You already have a magnificent suit of armour!\"")
                continue

            else:
                clear()
                print(f"You bought {armour_name}!")
                character['Gold'] -= armour_cost
                add_equipment(character, armour_name, armour_power, "Armour")

        elif choice == "3":
            clear()
            print("1. Health Potion $5\n2. AP Potion $10")
            potion_choice = input("Enter the number of the potion you want to buy: ")

            if potion_choice == "1":
                potion_cost = 10
                potion_name = "Health Potion"
                potion_power = 15

            elif potion_choice == "2":
                potion_cost = 10
                potion_name = "AP Potion"
                potion_power = 10

            else:
                clear()
                print("Invalid choice. Please enter a valid option.")
                continue

            if character['Gold'] < potion_cost:
                clear()
                print("Not enough gold to buy the potion.")

            else:
                clear()
                print(f"You bought a {potion_name}!")
                character['Gold'] -= potion_cost
                add_inventory(character, potion_name, potion_power, 1, "Consumable")

        elif choice == "4":
            clear()
            print(f"\"Thanks for visiting the Shop! Come again.\"")
            break

        else:
            clear()
            print("Invalid choice. Please choose a valid option (1, 2, 3, or 4).")

    return character


def add_equipment(character, item_name, item_power, item_type):
    for key, value in character['Inventory'].items():
        if value['Name'] == item_name:
            print(f"You already have {item_name} in your inventory.")
            return

        elif item_type == "Weapon" and value['Type'] == "Weapon":
            print(f"Replacing {value['Name']} with {item_name} in your inventory.")
            character['Attack'] -= value['Power']
            value['Name'] = item_name
            value['Power'] = item_power
            character['Attack'] += item_power

        elif item_type == "Armour" and value['Type'] == "Armour":
            print(f"Replacing {value['Name']} with {item_name} in your inventory.")
            character['Defence'] -= value['Power']
            value['Name'] = item_name
            value['Power'] = item_power
            character['Defence'] += item_power


def add_inventory(character, item_name, item_power, item_quantity, item_type):
    for key, value in character['Inventory'].items():
        if value['Name'] == item_name and value['Type'] == "Consumable":
            print(f"You added {item_quantity} {item_name}(s) to your inventory!")
            value['Quantity'] += item_quantity
            return
        elif value['Name'] == item_name and value['Type'] == "Special":
            print(f"You already have {item_name} in your inventory.")
            return

    # If the item is not in the inventory or is a non-consumable, add a new entry
    inventory_key_count = len(character['Inventory']) + 1
    new_item = {"Name": item_name, "Power": item_power, "Quantity": item_quantity, "Type": item_type}
    character['Inventory'][str(inventory_key_count)] = new_item
    print(f'You added {item_quantity} {item_name}(s) to your inventory!')


def combat_loop(character, foe):
    """
    Conduct the combat loop between the character and a foe.

    :param character: a non-empty dictionary representing the player character
    :param foe: a non-empty dictionary representing the foe
    :precondition: character must be alive with greater than 0 HP
    :precondition: foe must be alive with greater than 0 HP
    :postcondition: conducts the combat loop until either the character or the foe is defeated
    :return: returns True if the character wins, otherwise False

    # >>> combat_loop({'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5, 'Attack': 1, 'Armour': 0},
    # ... {'Name': 'Goblin', 'Attack': 2, 'Current HP': 10},
    # ... {(0, 0): "Starting Room", (1, 0): "Empty Room"})
    # True
    Dunno how to test yet. @patch?
    """
    while is_alive(character) and is_alive(foe):

        print(f"Your HP: {character['Current HP']}")
        print(f"Your AP: {character['Ability Points']}")
        print("Options:")
        print("1. Attack")
        print("2. Use Ability")
        print("3. Use Items")
        print("4. Check Enemy Stats")
        print("5. Run Away")

        action = input("Choose an option (1, 2, 3, or 4): ")

        if action == "1":
            clear()
            damage_dealt = max(0, character['Attack'] - foe['Defence'])
            foe['Current HP'] -= damage_dealt
            print(f"You dealt {damage_dealt} damage to the {foe['Name']}!")

            # Foe counterattacks
            if is_alive(foe):
                enemy_attack(character, foe)

        elif action == "2":
            clear()
            try:
                print("Choose an ability: ")
                for key, value in character['Abilities'].items():
                    print(f"{key}. \"{value['Name']}\" | Power: {value.get('Power', 0)} |"
                          f" AP Cost: {value.get('AP Cost', 0)}")

                skill_choice = input("Enter the number of the skill you want to use: ")

                if skill_choice in character['Abilities']:
                    clear()
                    ability = character['Abilities'][skill_choice]
                    ability_cost = ability.get('AP Cost', 0)

                    if character['Ability Points'] < ability_cost:
                        print("Insufficient Ability Points to use this skill.")
                        continue

                    damage_dealt = max(0, character['Attack'] + ability.get('Power', 0) - foe['Defence'])
                    foe['Current HP'] -= damage_dealt
                    print(f"You used {ability['Name']} and dealt {damage_dealt} damage to the {foe['Name']}!")
                    character['Ability Points'] -= ability_cost

                else:
                    raise ValueError("Invalid skill choice")

                if is_alive(foe):
                    enemy_attack(character, foe)

            except ValueError:
                print("Please enter a valid skill number.")
                continue

        elif action == "3":
            clear()
            try:
                # Check if there are any consumables in the inventory
                consumables_exist = any(item.get('Type') == "Consumable" for item in character['Inventory'].values())
                if consumables_exist:
                    print("Your Inventory:")
                    for key, value in character['Inventory'].items():
                        if value.get('Type') == "Consumable":
                            print(f"{key}. {value['Name']} x{value.get('Quantity', 0)}")

                else:
                    raise ValueError("No consumables in inventory")

            except ValueError as e:
                print(e)
                continue

            try:
                item_choice = input("Choose an item to use: ")
                use_item_success = use_item(character, item_choice)

                if not use_item_success:
                    continue

            except ValueError:
                print("Invalid input. Please enter a valid item number.")

        elif action == "4":
            clear()
            print(f"{foe['Name']}'s HP: {foe['Current HP']}")
            print(f"{foe['Name']}'s Attack: {foe['Attack']}")
            print(f"{foe['Name']}'s Defence: {foe['Defence']}")
            continue

        elif action == "5":
            clear()
            # Player chooses to run away
            print("You run away from the battle.")
            return False, character

        else:
            print("Invalid choice. Please choose a valid option (1, 2, 3, or 4).")

    if is_alive(foe):
        print(f"You were defeated by the {foe['Name']}. Game over!")
        return False
    else:
        battle_rewards(character, foe)

        return True, character


def enemy_attack(character, foe):
    """
    """
    # If the foe has a special ability and is below half health
    if 'Special Ability' in foe and foe['Current HP'] < foe['Max HP'] / 2 and foe['Special Ability Counter'] == 0:

        foe_special_ability_name = next(iter(foe['Special Ability']))
        foe_special_ability = foe['Special Ability'][foe_special_ability_name]
        ability_power = foe_special_ability.get('Power')
        foe_attack = foe['Attack'] + random.randint(-1, 1)

        total_damage = max(0, foe_attack + ability_power - character['Defence'])
        character['Current HP'] -= total_damage
        foe['Special Ability Counter'] += 1
        print(f"{foe_special_ability.get('Description')}")
        print(f"Your Radiant Blade and Guardian Armour are reacting to the {foe['Name']}'s special ability!")
        print(f"Your special items mitigate {foe_special_ability_name} and it only deals {total_damage} damage!")
        print(f"You sense that the creature is weakening.")

    # 25% to use ability
    elif random.random() < 0.25 and 'Ability' in foe:
        foe_ability_name = next(iter(foe['Ability']))
        foe_ability = foe['Ability'][foe_ability_name]
        ability_power = foe_ability.get('Power')
        foe_attack = foe['Attack'] + random.randint(-1, 1)

        total_damage = max(0, foe_attack + ability_power - character['Defence'])
        character['Current HP'] -= total_damage
        print(f"{foe_ability.get('Description')}")
        print(f"The {foe['Name']} uses {foe_ability_name} and deals {total_damage} damage!")

    else:
        foe_attack = foe['Attack'] + random.randint(-1, 1)
        total_damage = max(0, foe_attack - character['Defence'])
        character['Current HP'] -= total_damage
        print(f"The {foe['Name']} counterattacks and deals {total_damage} damage!")


def battle_rewards(character, foe):
    print(f"You defeated the {foe['Name']} and earned {foe['Gold']} gold!")
    character["Experience Points"] += foe['Experience Points']
    print(f"You gained {foe['Experience Points']} experience points!")
    character['Gold'] += foe['Gold']
    print(f"Your total gold is now {character['Gold']}.")

    # Check for special item in foe's inventory
    special_item = foe.get('Special Item')
    if special_item:
        print(f"You obtained a special item: {special_item}!")
        add_inventory(character, special_item, 0, 1, "Special")

    # Check for equipment item in foe's inventory
    equipment_item = foe.get('Equipment Item')
    if equipment_item == "Radiant Blade":
        print(f"You obtained a special item: {equipment_item}!")
        add_equipment(character, equipment_item, 8, "Weapon")
    elif equipment_item == "Guardian Armour":
        print(f"You obtained a special item: {equipment_item}!")
        add_equipment(character, equipment_item, 5, "Armour")


def use_item(character, item_key):
    """
    """
    try:
        selected_item = character['Inventory'][item_key]

        if selected_item['Quantity'] <= 0:
            print(f"You don't have any {selected_item['Name']} left.")
            return False

        if "Health Potion" in selected_item["Name"]:
            # Will add the lowest amount to character health. If character is already at max HP, nothing will be added.
            healing_amount = min(selected_item["Power"], character['Max HP'] - character['Current HP'])
            character['Current HP'] += healing_amount
            selected_item['Quantity'] -= 1

            print(f"You used a {selected_item['Name']} and healed {healing_amount} health!")
            return True

        elif "AP Potion" in selected_item["Name"]:
            # Will add the lowest amount to character AP. If character is already at max AP, nothing will be added.
            ap_amount = min(selected_item["Power"], character['Max AP'] - character['Ability Points'])
            character['Ability Points'] += ap_amount
            selected_item['Quantity'] -= 1

            print(f"You used a {selected_item['Name']} and restored {ap_amount} AP!")
            return True

        print(f"You can't use {selected_item['Name']} in combat.")
        return False

    except KeyError:
        print("Invalid item selection.")
        return False


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


def game(character=None):
    """
    Initialize the game
    """
    achieved_goal = False

    if character is None:
        rows = 5
        columns = 5
        board = make_board(rows, columns)
        character = make_character()
        describe_current_location(board, character)

    else:
        rows = 5
        columns = 5
        board = make_board(rows, columns)
        describe_current_location(board, character)

    while not achieved_goal:
        direction = get_user_choice(rows, columns, character)
        valid_move = validate_move(board, character, direction)
        if valid_move:
            clear()
            move_character(character, direction)
            player_location = (character["X-coordinate"], character["Y-coordinate"])
            describe_current_location(board, character)

            if board.get(player_location) in ["Winter Sanctum", "Inferno Lair"]:
                special_foe = generate_special_foe(board, character)
                print(f"You are facing {special_foe['Name']}!")

                combat_result = combat_loop(character, special_foe)

                if not combat_result:
                    break

                if character['Experience Points'] >= character['EXP to Level Up']:
                    level_up(character)

            elif (board.get(player_location) == "Ice Guardian Room"
                  and any(item['Name'] == "Frozen Orb" for item in character['Inventory'].values())):
                special_foe = generate_special_foe(board, character)
                print(f"You are facing {special_foe['Name']}!")

                combat_result = combat_loop(character, special_foe)

                if not combat_result:
                    break

                if character['Experience Points'] >= character['EXP to Level Up']:
                    level_up(character)

            elif (board.get(player_location) == "Fire Guardian Room"
                  and any(item['Name'] == "Flame Orb" for item in character['Inventory'].values())):
                special_foe = generate_special_foe(board, character)
                print(f"You are facing {special_foe['Name']}!")

                combat_result = combat_loop(character, special_foe)

                if not combat_result:
                    break

                if character['Experience Points'] >= character['EXP to Level Up']:
                    level_up(character)

            elif (board.get(player_location) == "Final Room"
                  and any(item['Name'] == "Radiant Blade" for item in character['Inventory'].values())
                  and any(item['Name'] == "Guardian Armour" for item in character['Inventory'].values())):
                special_foe = generate_special_foe(board, character)
                print(f"You are facing {special_foe['Name']}!")

                combat_result = combat_loop(character, special_foe)

                if not combat_result:
                    break

            elif board.get(player_location) == "Traveling Merchant":
                visit_shop(character)

            else:
                there_is_a_challenger = check_for_foes()
                if there_is_a_challenger:

                    # Generate a foe
                    foe = generate_foe()
                    print(f"You are facing a {foe['Name']}!")

                    # Combat loop
                    combat_result = combat_loop(character, foe)

                    if not combat_result:
                        break  # Player ran away from combat

                    # Check for level up
                    if character['Experience Points'] >= character['EXP to Level Up']:
                        level_up(character)

            describe_current_location(board, character)
            achieved_goal = check_win_condition(board, character)

        else:
            print("You cannot go that direction.")

        if character["Current HP"] == 0:
            print("You lost all your HP! You lose!")
            break

        if is_alive(character) and achieved_goal:
            print(f"You have beaten the Final Boss!")
            print("Congratulations, you win a life-time supply of your favourite chocolate!")
            break


def main():
    """
    Execute the start_menu function
    """
    clear()
    start_menu()


if __name__ == "__main__":
    main()

"""
Jason Chow
A00942129
"""
import random


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
                board[(row, column)] = "Chocolate Room"

            elif (row, column) == (2, 2):
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
    :postcondition: creates a character with the given starting location, HP, attack power, and armor
    :return: a dictionary with coordinates at 0, 0, 5 HP, 1 Attack Power, and 0 Armor

#     >>> make_character()
#     {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10, 'Attack Power': 1, 'Defence': 0, 'Inventory': [], \
# 'Level': 1, 'Experience Points': 0, 'EXP to Level Up': 10}
    """
    return {
        "X-coordinate": 0,
        "Y-coordinate": 0,
        "Max HP": 10,
        "Current HP": 10,
        "Attack Power": 1,
        "Defence": 0,
        "Abilities": {
            1: {"Name": "Slash", "Power": 2},
        },
        "Inventory": {
            1: {"Name": "Bronze Sword", "Power": 0, "Type": "Weapon"},
            2: {"Name": "Clothes", "Power": 0, "Type": "Armour"},
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
    print(f"Your current Attack Power is {character['Attack Power']}.")
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
    character["Current HP"] = character["Max HP"]
    character["Attack Power"] += 1
    character["Defence"] += 1
    character["Level"] += 1
    character['Experience Points'] -= character['EXP to Level Up']
    character['EXP to Level Up'] = int(character['EXP to Level Up'] * 1.5)
    print(f"Congratulations! You leveled up to Level {character['Level']}!")
    print(f"Your Max HP is now {character['Max HP']}.")
    print(f"Your Attack Power is now {character['Attack Power']}.")
    print(f"Your Defence is now {character['Defence']}.")

    return character


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


def get_user_choice(character):
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
        user_input = input("Please choose a direction (1, 2, 3, or 4) or get character status(5), inventory(6): ")

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
            get_character_stats(character)

        elif user_input == "6":
            get_character_inventory(character)

        else:
            print("Invalid choice. Please choose a valid option (1, 2, 3, or 4).")


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
    """
    Generate a foe with random attributes.

    :param: N/A
    :precondition: character must be alive with greater than 0 HP
    :postcondition: creates a foe dictionary with random attributes
    :return: a dictionary representing the foe with attributes like 'Attack Power' and 'HP'

    # >>> generate_foe()
    # {'Name': 'Goblin', 'Attack Power': 2, 'Current HP': 5}
    Dunno how to test yet. @patch?
    """
    foe_names = ["Goblin", "Orc", "Skeleton", "Dragon"]
    return {
        "Name": random.choice(foe_names),
        "Attack Power": random.randint(1, 2),
        "Current HP": random.randint(2, 4),
        "Defence": 0,
        "Gold": 50
    }


def check_location(board, character):
    """
    Check if user has reached the goal.

    :param board: a non-empty dictionary
    :param character: a non-empty dictionary
    :precondition: board must be a dictionary with x, y coordinates as a key, and a room name as a value
    :precondition: character must be a dictionary with x, y coordinates, and HP counter
    :precondition: character must be alive with greater than 0 HP
    :postcondition: checks if the user has reached the 'Chocolate Room'
    :return: returns True if player character is located at the 'Chocolate Room', otherwise False

    >>> board_test = {(0, 0): "Starting Room", (2, 2): "Chocolate Room"}
    >>> character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> check_location(board_test, character_test)
    False

    >>> board_test = {(0, 0): "Starting Room", (2, 2): "Chocolate Room"}
    >>> character_test = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 5}
    >>> check_location(board_test, character_test)
    True
    """
    x = character["X-coordinate"]
    y = character["Y-coordinate"]
    coordinate = (x, y)

    if board.get(coordinate) == "Chocolate Room":
        return True
    elif board.get(coordinate) == "Traveling Merchant":
        visit_shop(character)
        return False
    else:
        return False


def visit_shop(character):
    """
    """
    print("Welcome to the Shop!")

    while True:
        print("1. Buy Weapon")
        print("2. Buy Armor")
        print("3. Buy Health Potion")
        print("4. Leave Shop")
        print(f"You currently have {character['Gold']} gold.")
        choice = input("Choose an option (1, 2, 3, or 4): ")

        if choice == "1":
            weapon_cost = 10
            weapon_name = "Iron Sword"

            if character['Gold'] < weapon_cost:
                print("Not enough gold to buy the weapon.")
            elif any(item.get('Name') == weapon_name for item in character['Inventory'].values()):
                print(f"You already have {weapon_name} in your inventory.")
                continue
            else:
                print(f"You bought {weapon_name}!")
                character['Gold'] -= weapon_cost
                add_equipment(character, weapon_name, 2, "Weapon")

        elif choice == "2":
            armour_cost = 10
            armour_name = "Leather armour"

            if character['Gold'] < armour_cost:
                print("Not enough gold to buy the armour.")
            elif any(item.get('Name') == armour_name for item in character['Inventory'].values()):
                print(f"You already have {armour_name} in your inventory.")
                continue
            else:
                print(f"You bought {armour_name}!")
                character['Gold'] -= armour_cost
                add_equipment(character, armour_name, 1, "Armour")

        elif choice == "3":
            potion_cost = 5
            potion_name = "Health Potion"

            if character['Gold'] < potion_cost:
                print("Not enough gold to buy the health potion.")
            else:
                print(f"You bought a {potion_name}!")
                character['Gold'] -= potion_cost
                add_inventory(character, potion_name, 5, 1, "Consumable")

        elif choice == "4":
            print("Thanks for visiting the Shop! Come again.")
            break

        else:
            print("Invalid choice. Please choose a valid option (1, 2, 3, or 4).")

    return character


def add_equipment(character, item_name, item_power, item_type):
    for key, value in character['Inventory'].items():
        if value['Name'] == item_name:
            print(f"You already have {item_name} in your inventory.")
            return
        elif item_type == "Weapon" and value['Type'] == "Weapon":
            print(f"Replacing {value['Name']} with {item_name} in your inventory.")
            character['Attack Power'] -= value['Power']
            value['Name'] = item_name
            value['Power'] = item_power
            character['Attack Power'] += item_power

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

    # If the item is not in the inventory or is a non-consumable, add a new entry
    inventory_key_count = len(character['Inventory']) + 1
    new_item = {"Name": item_name, "Power": item_power, "Quantity": item_quantity, "Type": item_type}
    character['Inventory'][inventory_key_count] = new_item
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

    # >>> combat_loop({'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5, 'Attack Power': 1, 'Armor': 0},
    # ... {'Name': 'Goblin', 'Attack Power': 2, 'Current HP': 10},
    # ... {(0, 0): "Starting Room", (1, 0): "Empty Room"})
    # True
    Dunno how to test yet. @patch?
    """
    while is_alive(character) and is_alive(foe):
        print(f"Your HP: {character['Current HP']}")
        print(f"{foe['Name']}'s HP: {foe['Current HP']}")
        print("Options:")
        print("1. Attack")
        print("2. Use Ability")
        print("3. Use Items")
        print("4. Run Away")

        action = input("Choose an option (1, 2, 3, or 4): ")

        if action == "1":
            damage_dealt = max(0, character['Attack Power'] - foe['Defence'])
            foe['Current HP'] -= damage_dealt
            print(f"You dealt {damage_dealt} damage to the {foe['Name']}!")

            # Foe counterattacks
            if is_alive(foe):
                damage_taken = max(0, foe['Attack Power'] - character['Defence'])
                character['Current HP'] -= damage_taken
                print(f"The {foe['Name']} counterattacks and deals {damage_taken} damage!")

        elif action == "2":
            print("Choose an ability: ")
            for key, value in character['Abilities'].items():
                print(f"{key}. \"{value['Name']}\" | Power: {value.get('Power', 0)}")

            skill_choice = input("Enter the number of the skill you want to use: ")

            if int(skill_choice) in character['Abilities']:
                ability = character['Abilities'][int(skill_choice)]
                damage_dealt = max(0, character['Attack Power'] + ability['Power'] - foe['Defence'])
                foe['Current HP'] -= damage_dealt
                print(f"You used {ability['Name']} and dealt {damage_dealt} damage to the {foe['Name']}!")
            else:
                print("Invalid skill choice.")
                continue

            if is_alive(foe):
                damage_taken = max(0, foe['Attack Power'] - character['Defence'])
                character['Current HP'] -= damage_taken
                print(f"The {foe['Name']} counterattacks and deals {damage_taken} damage!")

        elif action == "3":
            consumables_exist = any(item.get('Type') == "Consumable" for item in character['Inventory'].values())

            if consumables_exist:
                print("Your Inventory:")
                for key, value in character['Inventory'].items():
                    if value.get('Type') == "Consumable":
                        print(f"{key}. {value['Name']} x{value.get('Quantity', 0)}")
            else:
                print("You have no consumables in your inventory.")
                continue

            item_choice = input("Choose an item to use: ")
            if item_choice.isdigit():
                use_item_success = use_item(character, int(item_choice))

                if not use_item_success:
                    continue

        elif action == "4":
            # Player chooses to run away
            print("You run away from the battle.")
            return False, character

        else:
            print("Invalid choice. Please choose a valid option (1, 2, 3, or 4).")

    if is_alive(foe):
        print(f"You were defeated by the {foe['Name']}. Game over!")
        return False
    else:
        print(f"You defeated the {foe['Name']} and earned {foe['Gold']} gold!")
        experience_gained = 15 if foe['Attack Power'] > character['Level'] else 10
        character["Experience Points"] += experience_gained
        print(f"You gained {experience_gained} experience points!")
        character['Gold'] += foe['Gold']
        print(f"Your total gold is now {character['Gold']}.")
        return True, character


def use_item(character, item_key):
    """
    """
    selected_item = character['Inventory'].get(item_key)

    if not selected_item:
        print("Invalid item selection.")
        return False

    if selected_item['Quantity'] <= 0:
        print(f"You don't have any {selected_item['Name']} left.")
        return False

    if "Health Potion" in selected_item["Name"]:
        healing_amount = selected_item["Power"]
        character['Current HP'] = min(character['Max HP'], character['Current HP'] + healing_amount)
        selected_item['Quantity'] -= 1

        print(f"You used a {selected_item['Name']} and healed {healing_amount} health!")
        return True

    print(f"You can't use {selected_item['Name']} in combat.")
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


def game():  # called from main
    """
    Initialize the game
    """
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character = make_character()
    achieved_goal = False

    while not achieved_goal:
        # Tell the user where they are
        describe_current_location(board, character)
        direction = get_user_choice(character)
        valid_move = validate_move(board, character, direction)

        if valid_move:
            move_character(character, direction)
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

            achieved_goal = check_location(board, character)

        else:
            print("You cannot go that direction.")

        if character["Current HP"] == 0:
            print("You lost all your HP! You lose!")
            break

        elif is_alive(character) and achieved_goal:
            print(f"You have arrived at the Chocolate Room!")
            print("Congratulations, you win a life-time supply of your favourite chocolate!")
            break


def main():
    """
    Execute the game function
    """
    game()


if __name__ == "__main__":
    main()

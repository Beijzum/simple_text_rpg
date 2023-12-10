import random
from unittest.mock import patch
from utility import draw_box


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

    >>> with patch('random.choice', return_value='Treasure Room'):
    ...     make_board(3, 3)
    {(0, 0): 'Starting Room', (0, 1): 'Treasure Room', (0, 2): 'Winter Sanctum', (1, 0): 'Treasure Room',\
 (1, 1): 'Traveling Merchant', (1, 2): 'Ice Guardian Room', (2, 0): 'Inferno Lair',\
 (2, 1): 'Fire Guardian Room', (2, 2): 'Final Room'}
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


def show_map(board_rows, board_columns, character):
    """
    Display the game map with the current player location, traveling merchant, special rooms, and boss room.

    :param board_rows: an integer representing the number of rows in the game board.
    :param board_columns: an integer representing the number of columns in the game board.
    :param character: a dictionary representing the player character, including their current location.
    :precondition: character must be alive with greater than 0 HP
    :precondition: board_rows must be an integer greater than 0.
    :precondition: board_columns must be an integer greater than 0.
    :precondition: character must be a dictionary with "X-coordinate" and "Y-coordinate" keys.
    :postcondition: prints the game map with the player character, traveling merchant, special rooms, and boss room.
    :return: a string representing the game map.

    >>> show_map(5, 5, {"X-coordinate": 0, "Y-coordinate": 0})
      ------------------------------------------------------
      | @Player  | (0, 1)   | (0, 2)   | (0, 3)   |#Special|
      ------------------------------------------------------
      | (1, 0)   | (1, 1)   | (1, 2)   | (1, 3)   | (1, 4) |
      ------------------------------------------------------
      | (2, 0)   | (2, 1)   | $Shop    | (2, 3)   | (2, 4) |
      ------------------------------------------------------
      | (3, 0)   | (3, 1)   | (3, 2)   | (3, 3)   |#Special|
      ------------------------------------------------------
      |#Special  | (4, 1)   | (4, 2)   |#Special  | #Boss  |
      ------------------------------------------------------
    """
    rows = board_rows
    columns = board_columns

    player_location = character["X-coordinate"], character["Y-coordinate"]

    for row in range(rows):
        print("  ------------------------------------------------------")
        for column in range(columns):
            position = (row, column)
            if position == player_location:
                print("  | @Player", end="")
            elif position == (int(rows / 2), int(columns / 2)):
                print("  | $Shop ", end=" ")
            elif position in [(rows - 1, 0), (0, columns - 1), (rows - 1, columns - 2), (rows - 2, columns - 1)]:
                print("  |#Special", end="")
            elif position == (rows - 1, columns - 1):
                print("  | #Boss ", end=" ")
            else:
                print(f"  | ({row}, {column})", end=" ")

        print("|")
    print("  ------------------------------------------------------")


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
        print("You sense a powerful dimensional anomaly in this area.")
        print("You must find the two special items to overcome this challenge.")


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
    >>> character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Inventory": {"1": {"Name": "Orb of Time"}}}
    >>> check_win_condition(board_test, character_test)
    False

    >>> board_test = {(0, 0): "Starting Room", (2, 2): "Final Room"}
    >>> character_test = {"X-coordinate": 2, "Y-coordinate": 2, "Inventory": {"1": {"Name": "Orb of Time"}}}
    >>> check_win_condition(board_test, character_test)
    True
    """
    x = character["X-coordinate"]
    y = character["Y-coordinate"]
    coordinate = (x, y)

    if (board.get(coordinate) == "Final Room"
            and any(item['Name'] == "Orb of Time" for item in character['Inventory'].values())):
        return True
    else:
        return False


def check_stronger_foe(character):
    """
    Check if the character has both the Frozen Orb and Flame Orb in their inventory.

    If both the Frozen Orb and Flame Orb are found in the character's inventory, the function will update the
    character's 'Stronger Enemies' status to True and print a message.

    :param character: a dictionary representing the player character
    :precondition: character must be alive with greater than 0 HP
    :precondition: character must have both the Frozen Orb and Flame Orb in their inventory
    :postcondition: changes 'Stronger Enemies' to True if both special items are found in the inventory.
    :return: changes 'Stronger Enemies' to True and prints a message if both special items are found in the inventory.

    >>> character_test = {"Inventory": {"1": {"Name": "Frozen Orb"}, "2": {"Name": "Flame Orb"}},\
"Stronger Enemies": False}
    >>> check_stronger_foe(character_test)
    +▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔+
    |  You sense the presence of stronger enemies in the dungeon.  |
    +▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁+
    True

    >>> character_test = {"Inventory": {"1": {"Name": "Frozen Orb"}}, "Stronger Enemies": False}
    >>> check_stronger_foe(character_test)
    False
    """
    frozen_orb_found = any(item['Name'] == "Frozen Orb" for item in character['Inventory'].values())
    flame_orb_found = any(item['Name'] == "Flame Orb" for item in character['Inventory'].values())

    if frozen_orb_found and flame_orb_found and not character['Stronger Enemies']:
        character['Stronger Enemies'] = True
        print(draw_box("You sense the presence of stronger enemies in the dungeon."))
        return True
    else:
        return False

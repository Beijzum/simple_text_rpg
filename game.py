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

            else:
                room = random.choice(room_list)
                board[(row, column)] = room

    return board


def make_character():
    """
    Create a character when invoking this function.

    :param: N/A
    :precondition: a dictionary with x, y coordinates, and HP counter
    :postcondition: creates a character with the given starting location and HP
    :return: a dictionary with coordinates at 0, 0 and 5 HP

    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    """
    return {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}


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


def get_user_choice():
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
        user_input = input("Please choose a direction (1, 2, 3, or 4): ")

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


def check_if_goal_attained(board, character):
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
    >>> check_if_goal_attained(board_test, character_test)
    False

    >>> board_test = {(0, 0): "Starting Room", (2, 2): "Chocolate Room"}
    >>> character_test = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 5}
    >>> check_if_goal_attained(board_test, character_test)
    True
    """
    x = character["X-coordinate"]
    y = character["Y-coordinate"]
    coordinate = (x, y)

    if board.get(coordinate) == "Chocolate Room":
        return True

    else:
        return False


def guessing_game(character):
    """
    Play a game where you have to guess a random number between 1 and 5.

    You must guess a random number between 1 and 5 until you get it correct. If you get it correct, then you beat the
    demon and can return to exploring the map. If you get it wrong, you lose 1 HP and you must play again until you beat
    the demon.

    :param character: a non-empty dictionary
    :precondition: character must be a dictionary with x, y coordinates, and HP counter
    :precondition: character must be alive with greater than 0 HP
    :postcondition: choosing the right number allows the character to leave the guessing game
    :postcondition: choosing the wrong number lowers player HP by 1, and you leave the guessing game
    :postcondition: inputting a string or float lowers player HP by 1, and you leave the guessing game
    :postcondition: if your HP is 0, then it is game over you must start the game again from a new character
    :return: returns an updated character HP if you win
    :return: returns a game over message if your health is 0
    """
    lower = 1
    upper = 5

    print(f"An annoying little demon stands in your way!")
    print(f"\"HellOoOoOOo~ You have to play a little game with me, adventurer.\"")
    print(f"\"You have to guess a number between {lower} and {upper}... OR ELSE!\"")
    print(f"\"My creator told me it also has be an *integer*, not a float or string.\"")

    while character["Current HP"] != 0:
        secret_number = random.randint(lower, upper)
        guess = input(f"Guess a number between {lower} and {upper}: ")

        if guess.isdigit():
            guess = int(guess)
            if guess == secret_number:
                print("\"Holy moly! How are you so smart?!\"")
                print("You kick the annoying little demon in the butt and it runs away.")
                print("\"AHHHHHHHH\"")
                print(f"Your current HP is {character['Current HP']}.")
                return character

            else:
                print(f"\"Hahaha! You're terrible at this! The number was {secret_number}.\"")
                print("The annoying little demon kicks your butt and you lose 1 HP.")
                print("\"Let's play again next time! Hahaha!\"")
                character["Current HP"] -= 1
                print(f"Your current HP is {character['Current HP']}.")
                return character

        else:
            print(f"\"That's not what I was asking for, idiot.\"")
            print("The annoying little demon bonks your head and you lose 1 HP.")
            print("\"I hope that clears your head. Hahaha!\"")
            character["Current HP"] -= 1
            print(f"Your current HP is {character['Current HP']}.")
            return character

    return character


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
    return True if character["Current HP"] != 0 else False


def game():  # called from main
    """
    Initialize the game
    """
    rows = 3
    columns = 3
    board = make_board(rows, columns)
    character = make_character()
    achieved_goal = False
    print(f"Your current HP is {character['Current HP']}.")

    while is_alive and not achieved_goal:
        # Tell the user where they are
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)

        if valid_move:
            move_character(character, direction)
            # describe_current_location(board, character) #unneccesary?
            there_is_a_challenger = check_for_foes()
            if there_is_a_challenger:
                guessing_game(character)
            achieved_goal = check_if_goal_attained(board, character)

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

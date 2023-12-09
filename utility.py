import os


def clear():
    """
    Clear the terminal screen for better readability.

    This function will use "cls" for a Windows OS, else it will use "clear".

    :param: N/A
    :precondition: user must trigger an event
    :precondition: user must be using a terminal
    :postcondition: terminal screen will be cleared
    :return: a cleared terminal screen

    >>> clear()

    """
    os.system("cls" if os.name == "nt" else "clear")


def draw_box(message: str) -> str:
    """
    Draw a box around a message.

    This function will draw a box around a message using unicode characters. It will be used for special events.

    :param message: a string
    :precondition: message must be a string
    :postcondition: prints a message enclosed in a box
    :return: a string representing the message enclosed in a box.
    """
    length = len(message) + 4
    top_border = "+" + "\u2594" * length + "+"
    bottom_border = "+" + "\u2581" * length + "+"

    box_message = f"{top_border}\n|  {message}  |\n{bottom_border}"
    return box_message


def draw():
    """
    Draw a horizontal line.

    :param: N/A
    :precondition: user must trigger an event
    :postcondition: prints a horizontal line
    :return: a string representing a horizontal line

    >>> draw()
    xX------------------------------------------------------Xx
    """
    print("xX------------------------------------------------------Xx")

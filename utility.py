import os


def clear():
    """
    Clear the terminal screen for better readability.

    This function will use "cls" for a Windows OS, else it will use "clear".
    """
    os.system("cls" if os.name == "nt" else "clear")


def draw_box(message):
    length = len(message) + 4
    top_border = "+" + "\u2594" * length + "+"
    bottom_border = "+" + "\u2581" * length + "+"

    box_message = f"{top_border}\n|  {message}  |\n{bottom_border}"
    return box_message


def draw():
    print("xX------------------------------------------------------Xx")

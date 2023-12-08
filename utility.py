import os


def clear():
    """
    Clear the terminal screen for better readability.

    This function will use "cls" for a Windows OS, else it will use "clear".
    """
    os.system("cls" if os.name == "nt" else "clear")

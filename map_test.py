import random

rows = 5
columns = 5

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

for row in range(rows):
    print("----------------------------------------------")
    for column in range(columns):
        print(f"| ({row}, {column})", end=" ")

    print("|")
print("----------------------------------------------")
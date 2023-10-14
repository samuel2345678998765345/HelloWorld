# The game function
def adventure_game():
    # The player starts in room 1
    room = 1

    # The game continues until the player reaches room 4 (the treasure room)
    while room != 4:
        # Room 1
        if room == 1:
            print("You are in room 1. There are doors to the east and south.")
            move = input("Which way do you want to go? ")
            if move == "east":
                room = 2
            elif move == "south":
                room = 3
            else:
                print("Invalid move. You can only go east or south.")

        # Room 2
        elif room == 2:
            print("You are in room 2. There are doors to the west and south.")
            move = input("Which way do you want to go? ")
            if move == "west":
                room = 1
            elif move == "south":
                room = 4
            else:
                print("Invalid move. You can only go west or south.")

        # Room 3
        elif room == 3:
            print("You are in room 3. There is a door to the north.")
            move = input("Which way do you want to go? ")
            if move == "north":
                room = 1
            else:
                print("Invalid move. You can only go north.")

    # Room 4 (the treasure room)
    print("Congratulations! You found the treasure!")

# Start the game
adventure_game()

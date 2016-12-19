import random

'''
List of moves, encoded in a list of lists, with each element containing both
a string literal with the name of the move, and a sub-list of win/lose/tie
states for each move. 1 represents a win, 0 is a loss, and -1 is a tie.
'''
MOVES = [['Punch of Fury', [-1, 0, 0, 1, 1, 0]],
         ['Kick of Punishment', [1, -1, 0, 0, 1, 0]],
         ['Sword of Justice', [1 , 1, -1, 0, 0, 1]],
         ['Shuriken of Vengeance', [0, 1, 1, -1, 0, 1]],
         ['Nunchucks of Anger', [0, 0, 1, 1, -1, 0]],
         ['Knife of Freedom', [1, 1, 0, 0, 1, -1]]]

WINMESSAGE = "Congratulations! You won!"
TIEMESSAGE = "You tied with the computer!"
LOSEMESSAGE = "Unfortunately, you have been defeated"


def input_name():
    name = input("Enter your name: ")
    return name


def get_move_name(move_number):
    # Check to make sure we're not out of bounds
    if 1 <= move_number <= 6:
        return MOVES[move_number - 1][0]
    else:
        return -1


def list_moves():
    # For every element in MOVES
    for i in range(0, 6):
        # Print the name of the move and the move number
        print("(" + str(i + 1) + ") " + MOVES[i][0])  # Uses a type conversion to avoid added spaces


def input_move():
    user_input = 0
    print("Pick a move.")
    list_moves()
    # Loop until the user enters a valid choice
    while not 1 <= user_input <= 6:
        user_input = int(input("Enter your selection: "))
    return user_input


def play():
    user_move = input_move()
    # Generate a random number between 1 and 6
    computer_move = random.randint(1, 6)
    print("You chose:", get_move_name(user_move))
    print("The computer chose:", get_move_name(computer_move))
    # Perform a simple comparison to check for a tie
    if user_move == computer_move:
        print(TIEMESSAGE)
    # Check for win condition
    elif MOVES[user_move - 1][1][computer_move - 1] == 1:
        print(WINMESSAGE)
    else:
        print(LOSEMESSAGE)


if __name__ == "__main__":
    print("Welcome to Ultimate Ninja Battle Combat!")
    user_name = input_name()
    print("Welcome, " + user_name)
    user_input = ""
    # Loop until the user chooses to quit
    while user_input != "Q":
        # Display a prompt, accept the user's input and convert it to upper case
        user_input = str(input("(I)nstructions\n(P)lay\n(Q)uit\nEnter your selection: ")).upper()
        if user_input == "I":
            print("Welcome to Ultimate Ninja Battle Combat!")
            print("You will be fighting against the computer, and the winner gets bragging rights.")
            print("For each turn you will be asked to use one of the 6 attacks below.")
            list_moves()
        elif user_input == "P":
            play()
        elif user_input != "Q":
            print("Invalid input. Please try again.")

    print("Thank you for playing Ultimate Ninja Battle Combat!")

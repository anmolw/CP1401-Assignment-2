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
    '''
    Prompts the user to enter their name.
    '''
    name = input("Enter your name: ")
    return name


def place_bet(balance):
    '''
    Let the user place a bet that is a multiple of 5 and less than or equal to
    their balance.
    '''
    bet = int(input("Please enter the amount to bet. All bets must be multiples of 5\nYou choose to bet $"))
    while bet % 5 != 0 or bet > balance:
        print("That is not a valid amount. Your bet must be a multiple of 5, and be within your means.")
        bet = int(input("Please enter the amount to bet. All bets must be multiples of 5\nYou choose to bet $"))
    return bet


def get_move_name(move_number):
    '''
    Return the name of a move, given its number
    '''
    # Check to make sure we're not out of bounds
    if 1 <= move_number <= 6:
        return MOVES[move_number - 1][0]
    else:
        return -1


def list_moves():
    '''
    Loop through the moves array and print the name of each move
    '''
    # For every element in MOVES
    for i in range(0, 6):
        # Print the name of the move and the move number
        print("({0}) {1}".format(i + 1, MOVES[i][0]))


def input_move():
    '''
    Prompt the user to pick a move from the list
    '''
    user_input = 0
    print("Pick a move.")
    list_moves()
    # Loop until the user enters a valid choice
    while not 1 <= user_input <= 6:
        user_input = int(input("Enter your selection: "))
    return user_input


def play():
    '''
    Main game function. Lets the user pick a move, and randomly chooses a
    computer move. Evaluates the result of the game.
    '''
    user_move = input_move()
    # Generate a random number between 1 and 6
    computer_move = random.randint(1, 6)
    print("You chose:", get_move_name(user_move))
    print("The computer chose:", get_move_name(computer_move))
    # Perform a simple comparison to check for a tie
    if user_move == computer_move:
        print(TIEMESSAGE)
        return 2
    # Check for win condition
    elif MOVES[user_move - 1][1][computer_move - 1] == 1:
        print(WINMESSAGE)
        return 1
    else:
        print(LOSEMESSAGE)
        return 0


def main():
    # Create an empty list
    balance_history = list()
    # Starting balance is $100
    balance = 100
    print("Welcome to Ultimate Ninja Battle Combat!")
    user_name = input_name()
    print("Welcome, " + user_name)
    user_input = None
    # Loop until the user chooses to quit
    while user_input != "Q":
        print("Your current balance is ${}".format(balance))
        # Display a prompt, accept the user's input and convert it to upper case
        user_input = str(input("Please choose from the following menu:\n(I)nstructions\n(P)lay\n(Q)uit\nEnter your selection: ")).upper()
        if user_input == "I":
            print("Welcome to Ultimate Ninja Battle Combat!")
            print("You will be fighting against the computer, and the winner gets bragging rights.")
            print("For each turn you will be asked to use one of the 6 attacks below.")
            list_moves()
        elif user_input == "P":
            # Quit if the user has 0 balance
            if balance == 0:
                break
            bet = place_bet(balance)
            result = play()
            if result == 0:
                # If the user lost
                balance -= bet
            elif result == 1:
                # If the user won
                balance += bet
            balance_history.append(balance)

        elif user_input != "Q":
            print("Invalid input. Please try again.")

    print("Goodbye {}. Your final balance is ${}".format(user_name, balance))
    print("Your balance history is:")
    print("Starting balance: $100")
    if balance_history:
        # Only print the per-round balance history if the user has actually played a round
        for i in range(0, len(balance_history)):
            print("After round {}: ${}".format(i+1, balance_history[i]))


main()

# Single player version of the classic game "Battleship"
board = []
# For the set ['O', 'O', 'O', 'O', 'O'], do it 5 times and add the additional one at the back.
for x in range(5):
    board.append(["O"] * 5)


# After this you will have a horizontal ['O', 'O', 'O', 'O', 'O'] in 5.

# Now we need to print the board in vertical format
def print_board(board):
    # We print the board in row, use loop, print 1 row, and then return nothing, print again until we print all 5.
    for row in board:
        # use 1 space as separator and join all the O together in a row
        print(" ".join(row))
    return


print("Let's play Battleship!")
print_board(board)


def random_row(board):
    # Load random module first. Generate a random row number(integer) and return it right away!
    import random
    return random.randint(0, len(board) - 1)


def random_col(board):
    # Load random module first. Generate a random column number(integer) and return it right away!
    import random
    return random.randint(0, len(board) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

from Tools.scripts.treesync import raw_input

# Use module 'raw_input'
for turn in range(4):
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))
    print(turn + 1)

    # If the inputs match the random generated integers, give good prompt, end the game with break
    # but if you miss them, based on the inputs;
    # if your inputs are completely out of the board, give 'not in the ocean' prompt,
    # if your inputs are within the ocean but no match, give 'missed battleship' prompt.
    # If you already enter 4 times and no match, give 'game over' prompt


    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break

    else:
        # if your input is over the board, print prompt.
        if guess_row not in range(5) and guess_col not in range(5):
            print("Oops, that's not even in the ocean.")

            # if you guess the same thing, print prompt.
        elif (guess_row == "X" and guess_col == "X"):
            print("You guessed that one already.")

        else:
            print("You missed my battleship!")
        # Mark the board with 'X' based on your raw input, 0 is start.
        board[guess_row][guess_col] = 'X'
        print_board(board)

    if turn == 3:
        print("Game Over")

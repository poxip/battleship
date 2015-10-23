from random import randint

def game():
    board = []

    for x in range(5):
        board.append(["O"] * 5)

    def print_board(board):
        for row in board:
            print " ".join(row)

    print "Let's play Battleship!"
    print_board(board)

    def random_row(board):
        return randint(0, len(board))

    def random_col(board):
        return randint(0, len(board[0]))

    ship_row = random_row(board)
    ship_col = random_col(board)
    ship_row_guess = ship_row -1
    ship_col_guess = ship_col -1

    count = 0
    warning = "Hey, that's not the number. Game over."
    again = "Do you want to play again? y/n\n"
    congratulations = "Congratulations! You sunk my battleship!"
    not_area = "Hey, that's not even on battle area!"
    already_shot = "You was shooting here already!"
    miss = "You missed my battleship!"
    farewell = "Bye!"

    while count <= 4:
        print "You tried: %s of 5 times" % count

        guess_row = raw_input("Guess Row:")
        try:
            int(guess_row)
        except ValueError:
            print warning
            break
        else:
            guess_row = int(guess_row)

        guess_col = raw_input("Guess Col:")
        try:
            int(guess_col)
        except ValueError:
            print warning
            break
        else:
            guess_col = int(guess_col)

        guess_row -= 1
        guess_col -= 1
        count += 1

        if guess_row == ship_row_guess and guess_col == ship_col_guess:
            print congratulations
            print_board(board)
            new_game = raw_input(again)
            if new_game == "yes" or new_game == "y":
                game()
            else:
                print farewell
        elif guess_row >= 5 or guess_col >= 5:
            print not_area
        elif (board[guess_row][guess_col] == "X"):
            print already_shot
        else:
            print miss
            board[guess_row][guess_col] = "X"
            print_board(board)
    else:
        print "Game over! Ship was on row %s" %ship_row, "and col %s" % ship_col
        board[ship_row -1][ship_col -1] = "="
        print_board(board)
        new_game = raw_input(again)
        if new_game == "yes" or new_game == "y":
            game()
        else:
            print farewell

game()

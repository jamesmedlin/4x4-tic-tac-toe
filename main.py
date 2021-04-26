import time

# 0|1|2|3
# 4|5|6|7
# 8|9|10|11
# 12|13|14|15

class Board:


    def __init__(self):
        self.board = ["."] * 16  # . for empty space, false for X, true for O
        # if turn is even, then its X's turn, if turn is odd then O's turn
        self.current_turn = 0
        self.executed_moves = []

    def reset_game(self):
        self.board = ["."] * 16  # . for empty space, false for X, true for O
        # if turn is even, then its X's turn, if turn is odd then O's turn
        self.current_turn = 0
        self.executed_moves = []

    # returns the current board
    def get_board(self):
        return self.board

    # Determines if the inputted move is legal
    def is_move_valid(self, pos):
        if pos < 0 or pos > 15:
            return False
        elif self.board[pos] != '.':
            return False
        else:
            return True

    # outputs board in text format
    def draw_board(self):
        board = self.board
        for i in range(0, 16):
                print('{}| '.format(board[i]))
                if i % 4 == 3:
                    print()
        print()

    # is this game over?
    # returns X if X has won, O if O has won, false if game is not over, and true if game is tied.
    def is_over(self):
        # boolean sat formula
        curr_board = self.get_board()


        # return X if X wins
        if (not(curr_board[0]) and not(curr_board[1]) and not(curr_board[2]) and not(curr_board[3])):
            return "X"
        if (not(curr_board[4]) and not(curr_board[5]) and not(curr_board[6]) and not(curr_board[7])):
            return "X"
        if (not(curr_board[8]) and not(curr_board[9]) and not(curr_board[10]) and not(curr_board[11])):
            return "X"
        if (not(curr_board[12]) and not(curr_board[13]) and not(curr_board[14]) and not(curr_board[15])):
            return "X"
        if (not(curr_board[0]) and not(curr_board[4]) and not(curr_board[8]) and not(curr_board[12])):
            return "X"
        if (not(curr_board[1]) and not(curr_board[5]) and not(curr_board[9]) and not(curr_board[13])):
            return "X"
        if (not(curr_board[2]) and not(curr_board[6]) and not(curr_board[10]) and not(curr_board[14])):
            return "X"
        if (not(curr_board[3]) and not(curr_board[7]) and not(curr_board[11]) and not(curr_board[15])):
            return "X"
        if (not(curr_board[0]) and not(curr_board[5]) and not(curr_board[10]) and not(curr_board[15])):
            return "X"
        if (not(curr_board[3]) and not(curr_board[6]) and not(curr_board[9]) and not(curr_board[12])):
            return "X"

        # return O if O wins
        if ((curr_board[0]) and (curr_board[1]) and (curr_board[2]) and (curr_board[3])):
            return "O"
        if ((curr_board[4]) and (curr_board[5]) and (curr_board[6]) and (curr_board[7])):
            return "O"
        if ((curr_board[8]) and (curr_board[9]) and (curr_board[10]) and (curr_board[11])):
            return "O"
        if ((curr_board[12]) and (curr_board[13]) and (curr_board[14]) and (curr_board[15])):
            return "O"
        if ((curr_board[0]) and (curr_board[4]) and (curr_board[8]) and (curr_board[12])):
            return "O"
        if ((curr_board[1]) and (curr_board[5]) and (curr_board[9]) and (curr_board[13])):
            return "O"
        if ((curr_board[2]) and (curr_board[6]) and (curr_board[10]) and (curr_board[14])):
            return "O"
        if ((curr_board[3]) and (curr_board[7]) and (curr_board[11]) and (curr_board[15])):
            return "O"
        if ((curr_board[0]) and (curr_board[5]) and (curr_board[10]) and (curr_board[15])):
            return "O"
        if ((curr_board[3]) and (curr_board[6]) and (curr_board[9]) and (curr_board[12])):
            return "O"




        # if none above return, check if all spots are filled, if they are, then game is a tie
        if "." in curr_board:
            return False
        else:
            return True


    # 0|1|2|3
    # 4|5|6|7
    # 8|9|10|11
    # 12|13|14|15


    # Player 'O' is max, in this case AI
    def max(self):

        # return value is:
            # MaxScore, SuggestedPos

        # values for MaxScore are:
        # -1 - loss
        # 0  - a tie
        # 1  - win

        # values for SuggestedPos are 0-->15 inclusive

        # Set MaxScore to -2 as it is worse than the worst case:
        maxS = -2

        pos = None

        result = self.is_over()

        # Check if game has come to an end, then return the evaluation for the next move
        if result == 'X': # win
            return (-1, 0)
        elif result == 'O': # loss
            return (1, 0)
        elif result == '.': # tie
            return (0, 0)

        for i in range(0, 3):
            if self.get_board()[i] == '.':
                # On the empty field player 'O' makes a move and calls Min
                # That's one branch of the game tree.
                self.get_board()[i] = 'O'
                (m, min_pos) = self.min()
                # change the maxScore value if new one is higher
                if m > maxS:
                    maxS = m
                    pos = i
                # resetting back the field to empty
                self.get_board()[i] = '.'
        return (maxS, pos)


def min(self):
    minS = 2
    pos = None
    result = self.is_over()

    if result == 'X':
        return (-1, 0)
    elif result == 'O':
        return (1, 0)
    elif result == '.':
        return (0, 0)

    for i in range(0, 15):
            if self.curr_board[i]== '.':
                self.curr_board[i] = 'X'
                (m, max_pos) = self.max()

                if m < minS:
                    minS = m
                    pos = i

                self.curr_board[i] = '.'

    return (minS, pos)

def play(self):
    while True:
        self.draw_board()
        self.result = self.is_over()

        # Printing the appropriate message if the game has ended
        if self.result != False:
            if self.result == 'X':
                print('The winner is X!')
            elif self.result == 'O':
                print('The winner is O!')
            elif self.result == '.':
                print("It's a tie!")

            self.reset_game()
            return

        # If it's player's turn
        if self.current_turn % 2 == 0: # this means it is X's turn

            while True:

                start = time.time()
                (maxS, pos) = self.min()
                end = time.time()
                print('Evaluation time: {}s'.format(round(end - start, 7)))
                print('Recommended move: {}'.format(pos))

                px = int(input('Insert the desired move location: '))

                (qx, qy) = (px, py)

                if self.is_valid(px, py):
                    self.current_state[px][py] = 'X'
                    self.player_turn = 'O'
                    break
                else:
                    print('The move is not valid! Try again.')

        # If it's AI's turn
        else:
            (m, px, py) = self.max()
            self.current_state[px][py] = 'O'
            self.player_turn = 'X'


# test main method
def main():
    trial_board = Board()
    trial_board.make_move(0)
    trial_board.make_move(9)
    trial_board.make_move(1)
    trial_board.make_move(7)
    trial_board.make_move(2)
    trial_board.make_move(8)
    trial_board.make_move(3)

    print(minimax(trial_board, 0))


main()











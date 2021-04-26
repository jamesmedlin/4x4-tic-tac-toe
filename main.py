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
                print('{}| '.format(board[i]), end =" ")
                if i % 4 == 3:
                    print()
        print()

    # is this game over?
    # returns X if X has won, O if O has won, false if game is not over, and true if game is tied.
    def is_over(self):
        # boolean sat formula
        curr_board = self.get_board()

        # return O if O wins
        if ((curr_board[0] != ".") and (curr_board[0] == curr_board[1] == curr_board[2] == curr_board[3])):
            if (not(curr_board[0])):
                return "X"
            else:
                return "O"
        if ((curr_board[4] != ".") and (curr_board[4] == curr_board[5] == curr_board[6] == curr_board[7])):
            if (not (curr_board[4])):
                return "X"
            else:
                return "O"
        if ((curr_board[8] != ".") and (curr_board[8] == curr_board[9] == curr_board[10] == curr_board[11])):
            if (not (curr_board[8])):
                return "X"
            else:
                return "O"
        if ((curr_board[12] != ".") and (curr_board[12] == curr_board[13] == curr_board[14] == curr_board[15])):
            if (not (curr_board[12])):
                return "X"
            else:
                return "O"
        if ((curr_board[0] != ".") and (curr_board[0] == curr_board[4] == curr_board[8] == curr_board[12])):
            if (not (curr_board[0])):
                return "X"
            else:
                return "O"
        if ((curr_board[1] != ".") and (curr_board[1] == curr_board[5] == curr_board[9] == curr_board[13])):
            if (not (curr_board[1])):
                return "X"
            else:
                return "O"
        if ((curr_board[2] != ".") and (curr_board[2] == curr_board[6]) and (curr_board[10]) and (curr_board[14])):
            if (not (curr_board[2])):
                return "X"
            else:
                return "O"
        if ((curr_board[3] != ".") and (curr_board[3] == curr_board[7] == curr_board[11] == curr_board[15])):
            if (not (curr_board[3])):
                return "X"
            else:
                return "O"
        if ((curr_board[0] != ".") and (curr_board[0] == curr_board[5] == curr_board[10] == curr_board[15])):
            if (not (curr_board[0])):
                return "X"
            else:
                return "O"
        if ((curr_board[3] != ".") and (curr_board[3] == curr_board[6] == curr_board[9] == curr_board[12])):
            if (not (curr_board[3])):
                return "X"
            else:
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

    def max_alpha_beta(self, alpha, beta):

        # return value is:
        # MaxScore, SuggestedPos

        # values for MaxScore are:
        # -1 - loss
        # 0  - a tie
        # 1  - win

        # values for SuggestedPos are 0-->15 inclusive

        # Set MaxScore to -2 as it is worse than the worst case:
        max_score = -2
        pos = None

        result = self.is_over()

        # Check if game has come to an end, then return the evaluation for the next move
        if result == 'X':  # win
            return (-1, 0)
        elif result == 'O':  # loss
            return (1, 0)
        elif result == '.':  # tie
            return (0, 0)

        for i in range(0, 16):
            if self.get_board()[i] == '.':
                # On the empty field player 'O' makes a move and calls Min
                # That's one branch of the game tree.
                self.get_board()[i] = 'O'
                (score_i, pos_i) = self.min_alpha_beta(alpha, beta)
                if score_i > max_score:
                    max_score = score_i
                    pos = i
                self.get_board()[i] = '.'

                if max_score >= beta:
                    return (max_score, pos)

                if max_score > alpha:
                    alpha = max_score

        return (max_score, pos)


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

        for i in range(0, 16):
                if self.curr_board[i]== '.':
                    self.curr_board[i] = 'X'
                    (m, max_pos) = self.max()

                    if m < minS:
                        minS = m
                        pos = i

                    self.curr_board[i] = '.'

        return (minS, pos)

    def min_alpha_beta(self, alpha, beta):

        min_score = 2

        min_pos = None

        result = self.is_over()

        if result == 'X':
            return (-1, 0)
        elif result == 'O':
            return (1, 0)
        elif result == '.':
            return (0, 0)

        for i in range(0, 15):
                if self.get_board()[i] == '.':
                    self.get_board()[i] = 'X'
                    (i_score, i_pos) = self.max_alpha_beta(alpha, beta)
                    if i_score < min_score:
                        min_score = i_score
                        min_pos = i
                    self.get_board()[i] = '.'

                    if min_score <= alpha:
                        return (min_score, min_pos)

                    if min_score < beta:
                        beta = min_score

        return (min_score, min_pos)

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
                    (max_score, max_pos) = self.min()
                    end = time.time()
                    print('Evaluation time: {}s'.format(round(end - start, 7)))
                    print('Recommended move: {}'.format(pos))

                    pos_in = int(input('Insert the desired move location: '))

                    max_pos = pos_in

                    if self.is_move_valid(pos_in):
                        self.get_board[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('The move is not valid! Try again.')

            # If it's AI's turn
            else:
                (m, px, py) = self.max()
                self.current_state[px][py] = 'O'
                self.player_turn = 'X'

    def play_alpha_beta(self):
     while True:
        self.draw_board()
        self.result = self.is_over()

        if self.result != False:
            if self.result == 'X':
                print('The winner is X!')
            elif self.result == 'O':
                print('The winner is O!')
            elif self.result == '.':
                print("It's a tie!")


            self.reset_game()
            return

        if self.current_turn % 2 == 0:

            while True:
                start = time.time()
                (score, pos) = self.min_alpha_beta(-2, 2)
                end = time.time()
                print('Evaluation time: {}s'.format(round(end - start, 7)))
                print('Recommended move: {}'.format(pos))

                input_pos = int(input('Insert the  coordinate: '))

                pos = input_pos

                if self.is_move_valid(pos):
                    self.current_state[pos] = 'X'
                    self.player_turn = 'O'
                    break
                else:
                    print('The move is not valid! Try again.')

        else:
            (score, pos) = self.max_alpha_beta(-2, 2)
            self.current_state[pos] = 'O'
            self.player_turn = 'X'


# test main method
def main():
    g = Board()
    g.get_board()[0] = True
    g.get_board()[1] = True
    g.get_board()[4] = False
    g.get_board()[5] = True
    g.get_board()[2] = False
    g.get_board()[8] = False


    g.play_alpha_beta()


if __name__ == "__main__":
    main()












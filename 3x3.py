import time

# 0|1|2|3
# 4|5|6|7
# 8|9|10|11
# 12|13|14|15

class Board:


    def __init__(self):
        self.board = ["."] * 9  # . for empty space, false for X, true for O
        # if turn is even, then its X's turn, if turn is odd then O's turn
        self.current_turn = 0
        self.executed_moves = []

    def reset_game(self):
        self.board = ["."] * 9 # . for empty space, false for X, true for O
        # if turn is even, then its X's turn, if turn is odd then O's turn
        self.current_turn = 0
        self.executed_moves = []

    # returns the current board
    def get_board(self):
        return self.board

    # Determines if the inputted move is legal
    def is_move_valid(self, pos):
        if pos < 0 or pos > 8:
            return False
        elif self.board[pos] != '.':
            return False
        else:
            return True

    # outputs board in text format
    def draw_board(self):
        board = self.board
        for i in range(0, 9):
            text = "O"
            if board[i] == False:
                text = "X"
            if board[i] == ".":
                text = "."
            print('{}| '.format(text), end =" ")
            if i % 3 == 2:
                print()
        print()


    #012
    #345
    #678
    # is this game over?
    # returns X if X has won, O if O has won, false if game is not over, and true if game is tied.
    def is_over(self):
        # boolean sat formula
        curr_board = self.get_board()

        # return O if O wins
        if ((curr_board[0] != ".") and (curr_board[0] == curr_board[1] == curr_board[2])):
            if (not(curr_board[0])):
                return "X"
            else:
                return "O"
        if ((curr_board[3] != ".") and (curr_board[3] == curr_board[4] == curr_board[5])):
            if (not (curr_board[3])):
                return "X"
            else:
                return "O"
        if ((curr_board[8] != ".") and (curr_board[6] == curr_board[7] == curr_board[8] )):
            if (not (curr_board[8])):
                return "X"
            else:
                return "O"
        if ((curr_board[0] != ".") and (curr_board[0] == curr_board[3] == curr_board[6])):
            if (not (curr_board[0])):
                return "X"
            else:
                return "O"
        if ((curr_board[1] != ".") and (curr_board[1] == curr_board[4] == curr_board[7] )):
            if (not (curr_board[1])):
                return "X"
            else:
                return "O"
        if ((curr_board[2] != ".") and (curr_board[2] == curr_board[5] == curr_board[8])):
            if (not (curr_board[2])):
                return "X"
            else:
                return "O"
        if ((curr_board[0] != ".") and (curr_board[0] == curr_board[4]) and (curr_board[8])):
            if (not (curr_board[0])):
                return "X"
            else:
                return "O"
        if ((curr_board[2] != ".") and (curr_board[2] == curr_board[4] == curr_board[6])):
            if (not (curr_board[2])):
                return "X"
            else:
                return "O"

        # if none above return, check if all spots are filled, if they are, then game is a tie
        if "." in curr_board:
            return False
        else:
            return True

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

        for i in range(0, 9):
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

        for i in range(0, 9):
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
                    self.get_board()[pos] = 'X'
                    self.current_turn += 1
                    break
                else:
                    print('The move is not valid! Try again.')

        else:
            (score, pos) = self.max_alpha_beta(-2, 2)
            self.get_board()[pos] = 'O'
            self.current_turn += 1


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












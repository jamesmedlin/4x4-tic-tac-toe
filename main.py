# test comment

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

    #outputs board in text format
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

        """
        #returns X if x wins O if O wins
        return ((curr_board[0] == False and curr_board[1] == False and curr_board[2] == False and
                 curr_board[3] == False) or
                (curr_board[0] == True and curr_board[1] == True and curr_board[2] == True and curr_board[3] == True) or
                (curr_board[4] == False and curr_board[5] == False and curr_board[6] == False and curr_board[
                    7] == False) or
                (curr_board[4] == True and curr_board[5] == True and curr_board[6] == True and curr_board[7] == True) or
                (curr_board[8] == False and curr_board[9] == False and curr_board[10] == False and curr_board[
                    11] == False) or
                (curr_board[8] == True and curr_board[9] == True and curr_board[10] == True and curr_board[
                    11] == True) or
                (curr_board[12] == False and curr_board[13] == False and curr_board[14] == False and curr_board[
                    15] == False) or
                (curr_board[12] == True and curr_board[13] == True and curr_board[14] == True and curr_board[
                    15] == True) or
                (curr_board[4] == False and curr_board[5] == False and curr_board[6] == False and curr_board[
                    7] == False) or
                (curr_board[4] == True and curr_board[5] == True and curr_board[6] == True and curr_board[7] == True) or
                (curr_board[0] == False and curr_board[4] == False and curr_board[8] == False and curr_board[
                    12] == False) or
                (curr_board[0] == True and curr_board[4] == True and curr_board[8] == True and curr_board[
                    12] == True) or
                (curr_board[1] == False and curr_board[5] == False and curr_board[9] == False and curr_board[
                    13] == False) or
                (curr_board[1] == True and curr_board[5] == True and curr_board[9] == True and curr_board[
                    13] == True) or
                (curr_board[2] == False and curr_board[6] == False and curr_board[10] == False and curr_board[
                    14] == False) or
                (curr_board[2] == True and curr_board[6] == True and curr_board[10] == True and curr_board[
                    14] == True) or
                (curr_board[3] == False and curr_board[7] == False and curr_board[11] == False and curr_board[
                    15] == False) or
                (curr_board[3] == True and curr_board[7] == True and curr_board[11] == True and curr_board[
                    15] == True) or
                (curr_board[0] == False and curr_board[5] == False and curr_board[10] == False and curr_board[
                    15] == False) or
                (curr_board[0] == True and curr_board[5] == True and curr_board[10] == True and curr_board[
                    15] == True) or
                (curr_board[3] == False and curr_board[6] == False and curr_board[9] == False and curr_board[
                    12] == False) or
                (curr_board[3] == True and curr_board[6] == True and curr_board[9] == True and curr_board[12] == True))
        """

        # if none above return, check if all spots are filled, if they are, then game is a tie
        if "." in curr_board:
            return True
        else:
            return False


    # 0|1|2|3
    # 4|5|6|7
    # 8|9|10|11
    # 12|13|14|15

    """
    # when game is won, returns who the winner is
    # 0 means X, 1 means O
    def winner(self):
        if not (self.is_won()):
            raise Exception('Winner method called on a game that is not over')
        else:
            return self.current_turn % 2

    # is this board in a tied state?
    def is_tied(self):
        return (not self.is_won()) and self.current_turn == 16

    # make a move to change the current game state
    #
    def make_move(self, position):
        if self.current_turn % 2 == 0:
            self.board[position] = False
        else:
            self.board[position] = True
        self.executed_moves.append(position)
        self.current_turn += 1

    def undo_last(self):
        move_pos = self.executed_moves.pop()

        self.board[move_pos] = 0
        self.current_turn -= 1


def minimax(board, player_val):
    if board.is_won():
        if board.winner() == player_val:
            return 1
        else:
            return -1
    if board.is_tied():
        return 0

    scores = []
    for move in board.get_valid_moves():
        board.make_move(move)
        scores.append(minimax(board, player_val))
        board.undo_last()

    return max(scores) if player_val == board.current_turn % 2 else min(scores)
    """

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
                    # Fixing the maxScore value if new one is higher
                    if m > maxS:
                        maxS = m
                        pos = i
                    # Setting back the field to empty
                    self.get_board()[i] = '.'
        return (maxS, pos)

def play(self):
    while True:
        self.draw_board()
        self.result = self.is_end()

        # Printing the appropriate message if the game has ended
        if self.result != None:
            if self.result == 'X':
                print('The winner is X!')
            elif self.result == 'O':
                print('The winner is O!')
            elif self.result == '.':
                print("It's a tie!")

            self.initialize_game()
            return

        # If it's player's turn
        if self.player_turn == 'X':

            while True:

                start = time.time()
                (m, qx, qy) = self.min()
                end = time.time()
                print('Evaluation time: {}s'.format(round(end - start, 7)))
                print('Recommended move: X = {}, Y = {}'.format(qx, qy))

                px = int(input('Insert the X coordinate: '))
                py = int(input('Insert the Y coordinate: '))

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











# test comment

# 0|1|2|3
# 4|5|6|7
# 8|9|10|11
# 12|13|14|15
class Board:

    def __init__(self):
        self.board = [0] * 16  # 0 for empty space, false for X, true for O
        # if turn is even, then its X's turn, if turn is odd then O's turn
        self.current_turn = 0
        self.executed_moves = []

    # returns the current board
    def get_board(self):
        return self.board

    # returns the current board
    def get_valid_moves(self):
        valid_moves = []
        for i in range(len(self.board)):
            if self.board[i] == 0:
                valid_moves.append(i)
        return valid_moves

    # is this board in a winning state?
    # true means game is won by a player
    def is_won(self):
        # boolean sat formula
        curr_board = self.get_board()

        return ((curr_board[0] == False and curr_board[1] == False and curr_board[2] == False and curr_board[
            3] == False) or
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

    # 0|1|2|3
    # 4|5|6|7
    # 8|9|10|11
    # 12|13|14|15

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











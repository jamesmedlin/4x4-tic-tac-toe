# test comment
class Board:
    board = [0] * 16 # 0 for empty space, false for X, true for O
    # if turn is even, then its X's turn, if turn is odd then O's turn
    current_turn = 0
    executed_moves = []

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
        return

    # when game is won, returns who the winner is
    # 0 means X, 1 means O
    def winner(self):
        if not(self.is_won()):
            raise Exception('Winner method called on a game that is not over')
        else:
            return self.current_turn % 2

    # is this board in a tied state?
    def is_tied(self):
        return (not self.is_winning()) and self.current_turn == 16

    # make a move to change the current game state
    #
    def make_move(self, position):
        if self.current_turn % 2 == 0:
            self.board[position] = False
        else:
            self.board[position] = True
        self.executed_moves.append(position)

    def undo_last(self):
        move_pos = self.executed_moves.pop()

        self.board[move_pos] = 0


def minimax(board, player_val):

    if board.is_won():
        if board.winner() == player_val:
            return 1
        else:
            return -1
    if board.is_tied():
        return 0


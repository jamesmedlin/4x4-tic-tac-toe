import time

class Board:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.board = [['.','.','.','.'],
                              ['.','.','.','.'],
                              ['.','.','.','.'],
                              ['.','.','.','.']]

        # Player X always plays first
        self.player_turn = 'X'

    def draw_board(self):
        for i in range(0, 4):
            for j in range(0, 4):
                print('{}|'.format(self.board[i][j]), end=" ")
            print()
        print()

    # Determines if the made move is a legal move
    def is_move_valid(self, px, py):
        if px < 0 or px > 3 or py < 0 or py > 3:
            return False
        elif self.board[px][py] != '.':
            return False
        else:
            return True

    # Checks if the game has ended and returns the winner in each case
    def is_over(self):
        # Vertical win
        for i in range(0, 3):
            if (self.board[0][i] != '.' and
                    self.board[0][i] == self.board[1][i] and
                    self.board[1][i] == self.board[2][i]):
                return self.board[0][i]

        # Horizontal win
        for i in range(0, 3):
            if (self.board[i] == ['X', 'X', 'X', 'X']):
                return 'X'
            elif (self.board[i] == ['O', 'O', 'O', 'O']):
                return 'O'

        # Main diagonal win
        if (self.board[0][0] != '.' and
                self.board[0][0] == self.board[1][1] and
                self.board[0][0] == self.board[2][2] and
                self.board[0][0] == self.board[3][3]):
            return self.board[0][0]

        # Second diagonal win
        if (self.board[0][3] != '.' and
                self.board[0][3] == self.board[1][2] and
                self.board[0][3] == self.board[2][1] and
                self.board[0][3] == self.board[3][0]):
            return self.board[0][3]

        # Is whole board full?
        for i in range(0, 4):
            for j in range(0, 4):
                # There's an empty field, we continue the game
                if (self.board[i][j] == '.'):
                    return None

        # It's a tie!
        return '.'

    def max(self, alpha, beta):
        max_score = -2
        px = None
        py = None

        result = self.is_over()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 4):
            for j in range(0, 4):
                if self.board[i][j] == '.':
                    self.board[i][j] = 'O'
                    (m, min_i, in_j) = self.min_alpha_beta(alpha, beta)
                    if m > max_score:
                        max_score = m
                        px = i
                        py = j
                    self.board[i][j] = '.'

                    # Next two ifs in Max and Min are the only difference between regular algorithm and minimax
                    if max_score >= beta:
                        return (max_score, px, py)

                    if max_score > alpha:
                        alpha = max_score

        return (max_score, px, py)

    def min(self, alpha, beta):

        min_score = 2

        qx = None
        qy = None

        result = self.is_over()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 4):
            for j in range(0, 4):
                if self.board[i][j] == '.':
                    self.board[i][j] = 'X'
                    (m, max_i, max_j) = self.max_alpha_beta(alpha, beta)
                    if m < min_score:
                        min_score = m
                        qx = i
                        qy = j
                    self.board[i][j] = '.'

                    if min_score <= alpha:
                        return (min_score, qx, qy)

                    if min_score < beta:
                        beta = min_score

        return (min_score, qx, qy)

    def play(self):
        while True:
            self.draw_board()
            self.result = self.is_over()

            if self.result != None:
                if self.result == 'X':
                    print('The winner is X!')
                elif self.result == 'O':
                    print('The winner is O!')
                elif self.result == '.':
                    print("It's a tie!")

                self.reset_game()
                return

            if self.player_turn == 'X':

                while True:
                    start = time.time()
                    (m, qx, qy) = self.min_alpha_beta(-2, 2)
                    end = time.time()
                    print('Evaluation time: {}s'.format(round(end - start, 7)))
                    print('Recommended move: X = {}, Y = {}'.format(qx, qy))

                    px = int(input('Insert the X coordinate: '))
                    py = int(input('Insert the Y coordinate: '))

                    qx = px
                    qy = py

                    if self.is_move_valid(px, py):
                        self.board[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('The move is not valid! Try again.')

            else:
                (m, px, py) = self.max_alpha_beta(-2, 2)
                self.board[px][py] = 'O'
                self.player_turn = 'X'

def main():
    g = Board()
    g.play_alpha_beta()

if __name__ == "__main__":
    main()
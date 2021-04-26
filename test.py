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
        self.current_turn = 'X'

    def board_output(self):
        for i in range(0, 4):
            for j in range(0, 4):
                print('{word}|'.format(word = self.board[i][j]), end=" ")
            print()
        print()

    # Determines if the made move is a legal move
    def is_move_valid(self, x_in, y_in):
        if x_in < 0 or x_in > 3 or y_in < 0 or y_in > 3:
            return False
        elif self.board[x_in][y_in] != '.':
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
        x_in = None
        y_in = None

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
                    (m, min_i, in_j) = self.min(alpha, beta)
                    if m > max_score:
                        max_score = m
                        x_in = i
                        y_in = j
                    self.board[i][j] = '.'

                    # Next two ifs in Max and Min are the only difference between regular algorithm and minimax
                    if max_score >= beta:
                        return (max_score, x_in, y_in)

                    if max_score > alpha:
                        alpha = max_score

        return (max_score, x_in, y_in)

    def min(self, alpha, beta):

        min_score = 2

        pos_x = None
        pos_y = None

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
                    (m, max_i, max_j) = self.max(alpha, beta)
                    if m < min_score:
                        min_score = m
                        pos_x = i
                        pos_y = j
                    self.board[i][j] = '.'

                    if min_score <= alpha:
                        return (min_score, pos_x, pos_y)

                    if min_score < beta:
                        beta = min_score

        return (min_score, pos_x, pos_y)

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

            if self.current_turn == 'X':

                while True:
                    start = time.time()
                    (m, pos_x, pos_y) = self.min(-2, 2)
                    end = time.time()
                    print('Evaluation time: {}s'.format(round(end - start, 7)))
                    print('Recommended move: X = {}, Y = {}'.format(pos_x, pos_y))

                    x_in = int(input('Insert the X coordinate: '))
                    y_in = int(input('Insert the Y coordinate: '))

                    pos_x = x_in
                    pos_y = y_in

                    if self.is_move_valid(x_in, y_in):
                        self.board[x_in][y_in] = 'X'
                        self.current_turn = 'O'
                        break
                    else:
                        print('The move is not valid! Try again.')

            else:
                (m, x_in, y_in) = self.max(-2, 2)
                self.board[x_in][y_in] = 'O'
                self.current_turn = 'X'

def main():
    g = Board()
    g.board[0][0] = 'X'
    g.board[0][1] = 'O'
    g.board[0][2] = 'X'
    g.board[0][3] = 'O'

    g.play()

if __name__ == "__main__":
    main()
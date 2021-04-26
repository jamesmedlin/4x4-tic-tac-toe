import time


class Board:
   def __init__(self):
       self.reset_game()

   def reset_game(self):
       # The tic-tac-toe board will be represented as a 2d array. Blanks will be represented as .'s for
       # graphical display and False = X's and True = O's for the moves.
       self.board = [['.', '.', '.', '.'],
                     ['.', '.', '.', '.'],
                     ['.', '.', '.', '.'],
                     ['.', '.', '.', '.']]

       # Player X plays first and is user controlled
       self.current_turn = 'X'

   # method for displaying the current state of the board (print and format)
   def board_output(self):
       for i in range(0, 4):
           for j in range(0, 4):
               print('{word} | '.format(word=self.board[i][j]), end=" ")
           print()
       print()

   # given an x and y posn, determines if the move is out of the board or has already been played
   def is_move_valid(self, x_in, y_in):
       if x_in < 0 or x_in > 3 or y_in < 0 or y_in > 3:
           return False
       elif self.board[x_in][y_in] != '.':
           return False
       else:
           return True

   # Checks if the game has ended and returns the winner in each case
   # Return cases: X - X wins, O - O wins, . - draw, None - game not finished
   def is_over(self):

       boolean_array = [['.', '.', '.', '.'],
                     ['.', '.', '.', '.'],
                     ['.', '.', '.', '.'],
                     ['.', '.', '.', '.']]

       for i in range(0, 4):
           for j in range(0, 4):
               if self.board[i][j] == 'X':
                   boolean_array[i][j] = False
               if self.board[i][j] == 'O':
                   boolean_array[i][j] = True
               else:
                   boolean_array[i][j] = '.'

               # return O if O wins
               if ((boolean_array[0][0] != ".") and
                       (boolean_array[0][0] == boolean_array[0][1] == boolean_array[0][2] == boolean_array[0][3])):
                   if (not (boolean_array[0][0])):
                       return "X"
                   else:
                       return "O"
               if ((boolean_array[1][0] != ".") and
                       (boolean_array[1][0] == boolean_array[1][1] == boolean_array[1][2] == boolean_array[1][3])):
                   if (not (boolean_array[1][0])):
                       return "X"
                   else:
                       return "O"
               if ((boolean_array[2][0] != ".") and
                       (boolean_array[2][0] == boolean_array[2][1] == boolean_array[2][2] == boolean_array[2][3])):
                   if (not (boolean_array[2][0])):
                       return "X"
                   else:
                       return "O"
               if ((boolean_array[3][0] != ".") and
                       (boolean_array[3][0] == boolean_array[3][1] == boolean_array[3][2] == boolean_array[3][3])):
                   if (not (boolean_array[3][0])):
                       return "X"
                   else:
                       return "O"
               if ((boolean_array[0][0] != ".")
                       and (boolean_array[0][0] == boolean_array[1][0] == boolean_array[2][0] == boolean_array[3][0])):
                   if (not (boolean_array[0][0])):
                       return "X"
                   else:
                       return "O"
               if ((boolean_array[0][1] != ".") and
                       (boolean_array[0][1] == boolean_array[1][1] == boolean_array[2][1] == boolean_array[3][1])):
                   if (not (boolean_array[0][1])):
                       return "X"
                   else:
                       return "O"
               if ((boolean_array[0][2] != ".") and
                       (boolean_array[0][2] == boolean_array[1][2] == (boolean_array[2][2]) == (boolean_array[2][3]))):
                   if (not (boolean_array[0][2])):
                       return "X"
                   else:
                       return "O"
               if ((boolean_array[0][3] != ".") and
                       (boolean_array[0][3] == boolean_array[1][3] == boolean_array[2][3] == boolean_array[3][3])):
                   if (not (boolean_array[0][3])):
                       return "X"
                   else:
                       return "O"
               if ((boolean_array[0][0] != ".") and
                       (boolean_array[0][0] == boolean_array[1][1] == boolean_array[2][2] == boolean_array[3][3])):
                   if (not (boolean_array[0][0])):
                       return "X"
                   else:
                       return "O"
               if ((boolean_array[0][3] != ".") and
                       (boolean_array[0][3] == boolean_array[1][2] == boolean_array[2][1] == boolean_array[3][0])):
                   if (not (boolean_array[3])):
                       return "X"
                   else:
                       return "O"

       # Draw check: if nobody has won yet, check if board has any empty spaces left
       for i in range(0, 4):
           for j in range(0, 4):
               if self.board[i][j] == '.':
                   return None

       return '.'

   # Max function: returns the max_score as well as the associated x and y
   def max(self, alpha, beta):
       max_score = -2
       x_in = None
       y_in = None

       result = self.is_over()

       if result == 'O':
           return 1, 0, 0
       elif result == 'X':
           return -1, 0, 0
       elif result == '.':
           return 0, 0, 0

       for i in range(0, 4):
           for j in range(0, 4):
               if self.board[i][j] == '.':
                   self.board[i][j] = 'O'
                   # Makes the move and calls for the corresponding min move to be made
                   (m, min_i, in_j) = self.min(alpha, beta)
                   # if this branch beats the current max reassign
                   if m > max_score:
                       x_in = i
                       y_in = j
                       max_score = m
                   # Reset the move (no move should be made here)
                   self.board[i][j] = '.'

                   # Check the current max vs the beta and alpha values. If outside threshold return or update.
                   if max_score >= beta:
                       return max_score, x_in, y_in

                   if max_score > alpha:
                       alpha = max_score
       # Represents the max as well as the x and y cords of the max move
       return max_score, x_in, y_in

   # Function for finding the min score. Returns that score and the associated x and y cords.
   def min(self, alpha, beta):

       # Initializes the min score and x and y cords as needed.
       min_score = 2
       pos_x = None
       pos_y = None
       # Check here for terminal states and return if one is reached
       result = self.is_over()

       # Return the winner based on the terminal check.
       if result == 'O':
           return 1, 0, 0
       elif result == 'X':
           return -1, 0, 0
       elif result == '.':
           return 0, 0, 0

       for i in range(0, 4):
           for j in range(0, 4):
               if self.board[i][j] == '.':
                   self.board[i][j] = 'X'
                   # Makes the move and calls for the corresponding max move to be made
                   (m, max_i, max_j) = self.max(alpha, beta)
                   # if this branch beats the current min reassign
                   if m < min_score:
                       pos_x = i
                       pos_y = j
                       min_score = m
                       # Reset the move (no move should be made here)
                   self.board[i][j] = '.'

                   # Check the current max vs the beta and alpha values. If outside threshold return or update.
                   if min_score <= alpha:
                       return min_score, pos_x, pos_y

                   if min_score < beta:
                       beta = min_score
       # Represents the min as well as the x and y cords of the min move
       return min_score, pos_x, pos_y

   # Method to start the game against the AI.
   def play(self):
       while True:
           # Initializes the board also gameover check
           self.board_output()
           self.result = self.is_over()

           if self.result != None:
               if self.result == 'O':
                   print('The winner is O!')
               elif self.result == 'X':
                   print('The winner is X!')
               elif self.result == '.':
                   print("It's a tie!")

               self.reset_game()
               return

           if self.current_turn == 'X':
               # X's Turn: Prompt to make move until valid coordinates are entered
               while True:
                   # Counts the elapsed time to calculate the move
                   start = time.time()
                   (m, pos_x, pos_y) = self.min(-2, 2)
                   end = time.time()
                   # Prints the results and the time of the search
                   print('Move computation time: {} seconds'.format(end - start))
                   print('Best computed move: X = {}, Y = {}'.format(pos_x, pos_y))
                   # Prompt for user inputs
                   x_in = int(input('Enter the X coordinate: '))
                   y_in = int(input('Enter the Y coordinate: '))

                   pos_x = x_in
                   pos_y = y_in
                   # Ensure the move is valid
                   if self.is_move_valid(x_in, y_in):
                       self.current_turn = 'O'
                       self.board[x_in][y_in] = 'X'
                       break
                   else:
                       print('Invalid move entered.')
           # CPU's turn. Simply compute their best move and switch the turn back
           else:
               (m, x_in, y_in) = self.max(-2, 2)
               self.current_turn = 'X'
               self.board[x_in][y_in] = 'O'



def main():
   # Initialize the board and load up a few moves (moves can be changed)
   g = Board()

   g.board[0][0] = 'X'
   g.board[0][1] = 'O'
   g.board[0][2] = 'X'
   g.board[0][3] = 'O'

   g.play()


# Run the full game
if __name__ == "__main__":
   main()



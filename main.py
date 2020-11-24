# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time


class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [['.', '.', '.'],
                              ['.', '.', '.'],
                              ['.', '.', '.']]
        # Player X always plays first
        self.player_turn = 'X'

    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()

    # Determines if it is a legal move or not
    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != '.':
            return False
        else:
            return True

    # Checks if the game has ended and returns the winner in each case
    def is_ended(self):
        # Vertical win
        for i in range(0, 3):
            if (self.current_state[0][i] != '.' and
                    self.current_state[0][i] == self.current_state[1][i] and
                    self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]

        # Horizontal win
        for i in range(0, 3):
            if (self.current_state[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.current_state[i] == ['O', 'O', 'O']):
                return 'O'

        # Main diagonal win
        if (self.current_state[0][0] != '.' and
                self.current_state[0][0] == self.current_state[1][1] and
                self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]

        # Second digital win
        if (self.current_state[0][2] != '.' and
                self.current_state[0][2] == self.current_state[1][1] and
                self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]

        # Is whole board full?
        for i in range(0, 3):
            for j in range(0, 3):
                if (self.current_state[i][j] == '.'):
                    return None

        # It is a tie
        return '.'

    # Player O is max, in this case AI
    def max(self):
        """possible values for maxv are:
        -1 is loss
        0 is ties
        1 is win"""

        # We set maxv to 2 which is worst than worst case
        maxv = -2
        px = None
        py = None

        result = self.is_ended()

        # If the game to an end, the func needs to return the evaluation func of the end.
        if result == 'X':
            return (-1, 0, 0)
        if result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    # On the empty field player 'O' makes a move and calls min
                    # That is on branch of the game tree.
                    self.current_state[i][j] = 'O'
                    (m, min_i, min_j) = self.min()
                    # Fixing maxv if neeeded
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    # Setting back the field to empty
                    self.current_state[i][j] = '.'
        return (maxv, px, py)

    """ Player 'X' is is min, in this case human"""

    def min(self):
        minv = 2
        qx = None
        qy = None

        result = self.is_ended()

        # If the game to an end, the func needs to return the evaluation func of the end.
        if result == 'X':
            return (-1, 0, 0)
        if result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    # On the empty field player 'O' makes a move and calls min
                    # That is on branch of the game tree.
                    self.current_state[i][j] = 'X'
                    (m, max_i, max_j) = self.max()
                    # Fixing maxv if neeeded
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    # Setting back the field to empty
                    self.current_state[i][j] = '.'
        return (minv, qx, qy)

    def play(self):
        while True:
            self.draw_board()
            self.result = self.is_ended()

            # Printing appropriate msg if the game has ended
            if self.result != None:
                if self.result == 'X':
                    print("The winner is X")
                elif self.result == 'O':
                    print("The winner is O")
                elif self.result == '.':
                    print("It is a tie")

                self.initialize_game()
                return

            # If it is a player's turn
            if self.player_turn == 'X':
                while True:

                    start = time.time()
                    (m, qx, qy) = self.min()
                    end = time.time()
                    print("Evaluation time: {}s".format(round(end - start, 7)))
                    print("Recommended move: X = {}, Y = {}".format(qx, qy))

                    px = int(input("Insert the X coordinate: "))
                    py = int(input("Insert the Y coordinate: "))

                    (qx, qy) = (px, py)

                    if self.is_valid(px, py):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print("The move is invalid! Try again.")

            # If it is AI's turn
            else:
                (m, px, py) = self.max()
                self.current_state[px][py] = 'O'
                self.player_turn = 'X'


def main():
    g = Game()
    g.play()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

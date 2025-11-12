# Improved Connect 4 Game
import unittest


class Connect4:
    ROWS = 6
    COLS = 7

    def __init__(self, rows=6, columns=7):
        self.ROWS = rows
        self.COLS = columns
        self.board = [[' ' for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self.current_player = 'X'
        self.winner = None  # add this since you test for it later

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def print_board(self):
        print("\nCurrent Board:")
        for row in self.board:
            print('|', end='')
            for cell in row:
                if cell == 'X':
                    print('\033[91mX\033[0m', end='|')  # Red for X
                elif cell == 'O':
                    print('\033[94mO\033[0m', end='|')  # Blue for O
                else:
                    print(' ', end='|')
            print()
        print('---------------')
        print(' 1 2 3 4 5 6 7')

    def drop_chip(self, column):
        if not (1 <= column <= self.COLS):
            return False

        for row in range(self.ROWS - 1, -1, -1):
            if self.board[row][column - 1] == ' ':
                self.board[row][column - 1] = self.current_player
                return True
        return False  # Column full

    def check_win(self, player):
        # Horizontal check
        for row in range(self.ROWS):
            for col in range(self.COLS - 3):
                if all(self.board[row][col + i] == player for i in range(4)):
                    return True

        # Vertical check
        for row in range(self.ROWS - 3):
            for col in range(self.COLS):
                if all(self.board[row + i][col] == player for i in range(4)):
                    return True

        # Diagonal (down-right)
        for row in range(self.ROWS - 3):
            for col in range(self.COLS - 3):
                if all(self.board[row + i][col + i] == player for i in range(4)):
                    return True

        # Diagonal (up-right)
        for row in range(3, self.ROWS):
            for col in range(self.COLS - 3):
                if all(self.board[row - i][col + i] == player for i in range(4)):
                    return True

        return False

    def is_full(self):
        """Check if the board is full."""
        return all(self.board[0][col] != ' ' for col in range(self.COLS))

    def play_game(self):
        """Main game loop."""
        print("Welcome to Connect 4!\n")
        while True:
            self.print_board()
            print(f"Player {self.current_player}'s turn.")

            try:
                column = int(input("Enter column (1-7): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 7.")
                continue

            if not self.drop_chip(column):
                print("Invalid move! Column is full or out of range. Try again.")
                continue

            if self.check_win(self.current_player):
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break

            if self.is_full():
                self.print_board()
                print("It's a tie! No more moves left.")
                break

            self.switch_player()


class TestConnect4Init(unittest.TestCase):
    def setUp(self):
        self.game = Connect4()

    def test_board_dimensions(self):
        self.assertEqual(len(self.game.board), 6)
        self.assertEqual(len(self.game.board[0]), 7)

    def test_board_is_empty(self):
        for row in self.game.board:
            for cell in row:
                self.assertEqual(cell, ' ')

    def test_default_current_player(self):
        self.assertEqual(self.game.current_player, 'X')

    def test_winner_starts_none(self):
        self.assertIsNone(self.game.winner)

    def test_custom_board_size(self):
        custom_game = Connect4(rows=4, columns=5)
        self.assertEqual(len(custom_game.board), 4)
        self.assertEqual(len(custom_game.board[0]), 5)


if __name__ == "__main__":
    unittest.main()

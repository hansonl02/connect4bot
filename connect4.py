# import calculate from bot

class Board:
    def __init__(self, x=7, y=6):
        """Create a Board with x columns and y rows"""
        self.columns = x
        self.rows = y
        self.board = [[False] * y] * x

    def play(self, player, column):
        assert column < self.columns and column > 0, "Error: Incorrect Column Size"
        if all(self.board[column]):
            print('Column is full!')
            return False
        else:
            i = 5
            slot = self.board[column][i]
            while slot:
                i -= 1
                slot = self.board[column][i]

            self.board[column][i] = player #1, 2 or 'X', 'O'

    def display(self):
        #function that will display board
        def display_row(y):
            row = '|'
            for x in range(self.columns):
                slot = self.board[x][y]
                if not slot:
                    slot = ' '
                row += '{0}|'.format(slot)
            return row

        for y in range(self.rows):
            print(display_row(y))
        print()

    # def turn(self, player):
    #     self.display()
    #     self.check_winner()
    #     if player == 1: #human player
    #         col = input()
    #         self.play(player, col)
    #     else: #AI
    #         col = calculate()
    #         self.play(player, col)

b = Board()
b.display()
b.play(1, 2)
b.display()


  
class Board:
    def __init__(self, x=7, y=6):
        """Create a Board with x columns and y rows"""
        self.columns = x
        self.rows = y
        self.board = [[False for row in range(y)] for col in range(x)]

    def update_slot(self, player, x, y):
        print('haha')
        self.board[x][y] = player

    def get_slot(self, x, y):
        return self.board[x][y]

    def update_slot(self, player, x, y):
        self.board[x][y] = player
        return self.get_slot(x, y)

    def play(self, player, column):
        for slot in range(self.rows):
            if not self.get_slot(column, slot):
                self.board[column][slot] = player
                return
        print('Column is full!')
        return False

    def display_row(self, y):
        row = '|'
        for column in range(self.columns):
            slot = self.get_slot(column, y)
            if not slot:
                slot = ' '
            row += str(slot) + "|"
        return row

    def display_board(self):
        columns = 'col '
        for x in range(self.columns):
            columns += str(x) + ' '
        print(columns)
        for y in range(self.rows - 1, -1, -1):
            print('  ', self.display_row(y), 'row', y)
        print()

    def turn(self, player):
        self.display()
        self.check_winner()
        if player == 1: #human player
            col = input()
            self.play(player, col)
        else: #AI
            col = calculate()
            self.play(player, col)

b = Board()
b.play(1, 0)
b.display_board()

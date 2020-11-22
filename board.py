class Board:
    def __init__(self, x=7, y=6):
        """Create a Board with x columns and y rows"""
        self.columns = x
        self.rows = y
        self.board = [[False for row in range(y)] for col in range(x)]

    def update_slot(self, player, x, y):
        self.board[x][y] = player

    def get_slot(self, x, y):
        return self.board[x][y]

    def update_slot(self, player, x, y):
        self.board[x][y] = player
        return self.get_slot(x, y)

    def play(self, player, column):
        for slot in range(self.rows):
            if not self.get_slot(column, slot):
                self.update_slot(player, column, slot)
                return slot
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
        print()
        columns = 'col '
        for x in range(self.columns):
            columns += str(x) + ' '
        print(columns)
        for y in range(self.rows - 1, -1, -1):
            print('  ', self.display_row(y), 'row', y)
        print()

    def turn(self, player):
        self.display_board()
        # self.check_winner()
        if player == 1: # human player
            col = int(input('Which column would you like to drop a piece in? '))
            if col > self.columns:
                print('Invalid column number!')
                return False
            slot = self.play(player, col)
            print('Player {0} dropped a piece in slot ({1}, {2})!'.format(player, col, slot))
        # else: # AI
            # col = calculate()
            # self.play(player, col)

b = Board(10, 10)
b.turn(1)
b.play(2, 0)
b.turn(1)
b.play(2, 1)
b.turn(1)

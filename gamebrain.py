class GameBrain:
    """Assess the board conditions by placing a move, whether a space is occupied, or win conditions"""

    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def is_occupied(self, row, col):
        row_pos = int(row) - 1
        col_pos = int(col) - 1
        if self.board[row_pos][col_pos] == "X" or self.board[row_pos][col_pos] == "O":
            return True

    def place_move(self, row, col, player):
        row_pos = int(row) - 1
        col_pos = int(col) - 1

        self.board[row_pos][col_pos] = player

    def is_winning(self, player):
        # Check Horizontal Row
        for n in range(0, 3):
            if self.board[n].count(player) == 3:
                return True

        # Check Column
        for n in range(0, 3):
            col = list(zip(*self.board))[n]
            if col.count(player) == 3:
                return True

        # Check Diagonal
        diag_1 = [self.board[n][n] for n in range(0, 3)]
        diag_2 = [self.board[n][2 - n] for n in range(0, 3)]
        if diag_1.count(player) == 3 or diag_2.count(player) == 3:
            return True




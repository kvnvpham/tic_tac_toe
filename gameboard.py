class GameBoard:
    """Sets the game board's layout"""

    def __init__(self, game_brain):
        self.brain = game_brain

    def set_board(self):
        board_layout = f"{self.brain.board[0][0]} | {self.brain.board[0][1]} | {self.brain.board[0][2]}\n" \
                       f"_________\n" \
                       f"{self.brain.board[1][0]} | {self.brain.board[1][1]} | {self.brain.board[1][2]}\n" \
                       f"_________\n" \
                       f"{self.brain.board[2][0]} | {self.brain.board[2][1]} | {self.brain.board[2][2]}"
        return board_layout

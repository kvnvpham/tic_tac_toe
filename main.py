from players import Players
from gamebrain import GameBrain
from gameboard import GameBoard


def show_move(row, col, player):
    game_brain.place_move(row, col, player)
    print(game_board.set_board())


players = Players()
game_brain = GameBrain()
game_board = GameBoard(game_brain)

print("Ready to play Tic-Tac-Toe?")
print(game_board.set_board())
round = 1

while True:
    if round == 1:
        p1_turn = input(
            "Player 1, Where would you like to place your move?\n"
            "Enter row and column number separated by ', ' (e.g. 1, 2):  "
        )
    else:
        p1_turn = input("Player 1, Where would you like to place your move? ")

    p1_row, p1_col = p1_turn.split(", ")

    if game_brain.is_occupied(p1_row, p1_col):
        print("Sorry, that position is already taken.")

        p1_turn = input("Player 1, Where would you like to place your move? ")
        p1_row, p1_col = p1_turn.split(", ")
        show_move(p1_row, p1_col, players.p1)
    else:
        show_move(p1_row, p1_col, players.p1)

    if game_brain.is_winning(players.p1):
        print("Player 1 Wins! 😊")
        break

    p2_turn = input("Player 2, Where would you like to place your move? ")
    p2_row, p2_col = p2_turn.split(", ")

    if game_brain.is_occupied(p2_row, p2_col):
        print("Sorry, that position is already taken.")

        p2_turn = input("Player 2, Where would you like to place your move? ")
        p2_row, p2_col = p2_turn.split(", ")
        show_move(p2_row, p2_col, players.p2)
    else:
        show_move(p2_row, p2_col, players.p2)

    if game_brain.is_winning(players.p2):
        print("Player 2 Wins! 😊")
        break

    round += 1

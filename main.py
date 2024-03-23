from print_board import print_board
from valid_moves import valid_move
from utils import is_game_finished
from utils import execute_move

def main() -> None:
    board = ['K', 'Q', 'R', 'B', 'N', 'P', ' ', ' ', ' ', ' ', 'p', 'n', 'b', 'r', 'q', 'k']
    game_finished = False
    while not game_finished:
        print_board(board)
        move = input("Move: ")
        if valid_move(board, move):
            execute_move(board, move)
        else:
            print("Error: Invalid move")
        game_finished = is_game_finished(board)

if __name__ == "__main__":
    main()

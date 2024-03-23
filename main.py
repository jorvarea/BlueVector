from print_board import print_board
from valid_moves import valid_move
from utils import is_game_finished
from utils import execute_move
from minimax import minimax

SEARCH_DEPTH = 6

def main() -> None:
    board = ['K', 'Q', 'R', 'B', 'N', 'P', ' ', ' ', ' ', ' ', 'p', 'n', 'b', 'r', 'q', 'k']
    game_finished = False
    print_board(board)
    while not game_finished:
        move = input("Move: ")
        while not valid_move(board, move):
            print("Error: Invalid move")
            move = input("Move: ")
        execute_move(board, move)
        print_board(board)
        game_finished = is_game_finished(board)
        if not game_finished:
            _, minimax_move = minimax(board, SEARCH_DEPTH, 'black')
            execute_move(board, minimax_move)
            print(f"BlueVector played {minimax_move}")
            print_board(board)
            game_finished = is_game_finished(board)


if __name__ == "__main__":
    main()

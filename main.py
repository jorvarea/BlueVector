from print_board import print_board
from valid_moves import valid_move

def is_game_finished(board: list[str]):
    is_finished = False
    try:
        board.index('K')
        board.index('k')
    except ValueError:
        is_finished = True
    return is_finished

def execute_move(board: list[str], move: str) -> None:
    piece = move[0]
    next_position = int(move[1:])
    position = board.index(piece)
    board[position] = ' '
    board[next_position] = piece

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

from print_board import print_board
from valid_moves import valid_move
from utils import is_game_finished
from utils import execute_move
from minimax import minimax

SEARCH_DEPTH = 8
INFINITY = 9999

def print_header() -> None:
    print("Welcome to one-dimensional chess!")
    print("This chess variant is based on the one proposed by Dan Glimne in 1977")
    print("You can find the rules at https://docpop.itch.io/1d-chess")
    print("\nTo make a move, enter it in the format: <piece letter><target square>")
    print("k: king, q: queen, r: rook, b: bishop, n: knight, p: pawn")
    print("Note: Use uppercase letters for White pieces, lowercase for Black")
    print("\nYou'll be playing against BlueVector, an AI agent based on the legendary Deep Blue")
    print("Are you ready for the challenge?")

def get_color_choice() -> str:
    player_choice = input("\nChoose white(w) or black(b): ")
    while player_choice not in ("w", "b"):
        print("Error: Invalid choice")
        player_choice = input("Choose white(w) or black(b): ")
    return player_choice

def right_color_move(move: str, player_choice: str) -> bool:
    is_right_color = ((player_choice == 'w' and move[0].isupper())
                      or (player_choice == 'b' and move[0].islower()))
    return is_right_color

def get_player_move(board: list[str], player_choice: str) -> str:
    move = input("Your move: ")
    while not move or not valid_move(board, move) or not right_color_move(move, player_choice):
        print("Error: Invalid move")
        move = input("Your move: ")
    return move

def player_as_white(board: list[str]) -> bool:
    move = get_player_move(board, 'w')
    execute_move(board, move)
    print_board(board)
    game_finished = is_game_finished(board)
    if not game_finished:
        _, minimax_move = minimax(board, SEARCH_DEPTH, -INFINITY, INFINITY, 'black')
        execute_move(board, minimax_move)
        print(f"BlueVector's move: {minimax_move}")
        print_board(board)
        game_finished = is_game_finished(board)
    return game_finished

def player_as_black(board: list[str]) -> bool:
    _, minimax_move = minimax(board, SEARCH_DEPTH, -INFINITY, INFINITY, 'white')
    execute_move(board, minimax_move)
    print(f"BlueVector's move: {minimax_move}")
    print_board(board)
    game_finished = is_game_finished(board)
    if not game_finished:
        move = get_player_move(board, 'b')
        execute_move(board, move)
        print_board(board)
        game_finished = is_game_finished(board)
    return game_finished

def main() -> None:
    board = ['K', 'Q', 'R', 'B', 'N', 'P', ' ', ' ', ' ', ' ', 'p', 'n', 'b', 'r', 'q', 'k']
    game_finished = False
    print_header()
    player_choice = get_color_choice()
    print_board(board)
    while not game_finished:
        if player_choice == 'w':
            game_finished = player_as_white(board)
        else:
            game_finished = player_as_black(board)

if __name__ == "__main__":
    main()

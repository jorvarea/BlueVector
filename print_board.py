BG_BLUE = "\033[44m"
BG_CYAN = "\033[46m"
BLACK = "\033[30m"
WHITE = "\033[37m"
RESET = "\033[0m"

PIECE_ICONS = {
    'r': '♜',
    'n': '♞',
    'b': '♝',
    'q': '♛',
    'k': '♚',
    'p': '♟',
    ' ': ' '
}

def print_header() -> None:
    for i in range(16):
        print(f"{i:<3}", end='')
    print()

def print_board(board: list[str]):
    print_header()
    for i, piece in enumerate(board):
        bg_color = BG_BLUE if i % 2 == 0 else BG_CYAN
        piece_color = WHITE if piece.isupper() else BLACK
        piece_symbol = PIECE_ICONS[piece.lower()]
        print(f"{bg_color}{piece_color} {piece_symbol} {RESET}", end='')
    print()

def main() -> None:
    board = ['K', 'Q', 'R', 'B', 'N', 'P', ' ', ' ', ' ', ' ', 'p', 'n', 'b', 'r', 'q', 'k']
    print_board(board)

if __name__ == "__main__":
    main()

from typing import Final

# Changeable

SEARCH_DEPTH: Final[int] = 8
PIECE_VALUE: Final[dict[str, int]] = {
    'k': 100,
    'q': 9,
    'r': 5,
    'b': 3,
    'n': 3,
    'p': 1
}

# Constants

INFINITY: Final[int] = 9999
INITIAL_WHITE_PAWN_POSITION: Final[int] = 5
INITIAL_BLACK_PAWN_POSITION: Final[int] = 10

# Decorative configurations #

PIECE_ICONS: Final[dict[str, str]] = {
    'r': '♜',
    'n': '♞',
    'b': '♝',
    'q': '♛',
    'k': '♚',
    'p': '♟',
    ' ': ' '
}

BG_BLUE: Final[str] = "\033[44m"
BG_CYAN: Final[str] = "\033[46m"
BLACK: Final[str] = "\033[30m"
WHITE: Final[str] = "\033[37m"
RESET: Final[str] = "\033[0m"

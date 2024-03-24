from typing import Final

PIECE_VALUE: Final[dict[str, int]] = {
    'k': 100,
    'q': 9,
    'r': 5,
    'b': 3,
    'n': 3,
    'p': 1
}

def evaluation_function(board: list[str]) -> int:
    evaluation = 0
    for piece in board:
        if piece != ' ':
            if piece.isupper():
                evaluation += PIECE_VALUE[piece.lower()]
            else:
                evaluation -= PIECE_VALUE[piece.lower()]
    return evaluation

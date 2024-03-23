PIECE_VALUE = {
    'k': 100,
    'q': 9,
    'r': 5,
    'b': 3,
    'n': 3,
    'p': 1
}

def evaluating_function(board: list[str]) -> int:
    evaluation = 0
    for piece in board:
        if piece.isupper():
            evaluation += PIECE_VALUE[piece]
        else:
            evaluation -= PIECE_VALUE[piece]
    return evaluation

from config import PIECE_VALUE

def evaluation_function(board: list[str], depth: int) -> int:
    evaluation = 0
    for piece in board:
        if piece != ' ':
            if piece.isupper():
                evaluation += PIECE_VALUE[piece.lower()]
            else:
                evaluation -= PIECE_VALUE[piece.lower()]
    if 'K' not in board:
        evaluation -= depth
    if 'k' not in board:
        evaluation += depth
    return evaluation

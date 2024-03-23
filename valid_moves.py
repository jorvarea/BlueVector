INITIAL_WHITE_PAWN_POSITION = 5
INITIAL_BLACK_PAWN_POSITION = 10

def square_allowed(board: list[str], piece: str, next_position: int) -> bool:
    is_allowed = (board[next_position] == ' '
                  or (piece.isupper() and board[next_position].islower())
                  or (piece.islower() and board[next_position].isupper()))
    return is_allowed

def valid_pawn_move(board: list[str], piece: str, next_position: int) -> bool:
    try:
        piece_position = board.index(piece)
        if piece.isupper():
            is_valid = (square_allowed(board, piece, next_position)
                        and (next_position == piece_position + 1
                             or (piece_position == INITIAL_WHITE_PAWN_POSITION
                                 and next_position == INITIAL_WHITE_PAWN_POSITION + 2
                                 and board[next_position] == ' ')))
        else:
            is_valid = (square_allowed(board, piece, next_position)
                        and (next_position == piece_position - 1
                             or (piece_position == INITIAL_BLACK_PAWN_POSITION
                                 and next_position == INITIAL_BLACK_PAWN_POSITION - 2
                                 and board[next_position] == ' ')))
    except ValueError:
        is_valid = False
    return is_valid

def valid_knight_move(board: list[str], piece: str, next_position: int) -> bool:
    try:
        piece_position = board.index(piece)
        valid_position_set = {piece_position + 2, piece_position - 2,
                              piece_position + 3, piece_position - 3}
        is_valid = (square_allowed(board, piece, next_position)
                    and next_position in valid_position_set)
    except ValueError:
        is_valid = False
    return is_valid

def bishop_unblocked(board: list[str], piece_position: int, next_position: int) -> bool:
    is_unblocked = True
    step = 2 if piece_position < next_position else -2
    next_same_color_position = (piece_position + 2 if piece_position < next_position
                                else piece_position - 2)
    for position in range(next_same_color_position, next_position, step):
        if board[position] != ' ':
            is_unblocked = False
    return is_unblocked

def valid_bishop_move(board: list[str], piece: str, next_position: int) -> bool:
    try:
        piece_position = board.index(piece)
        is_valid = (square_allowed(board, piece, next_position)
                    and piece_position % 2 == next_position % 2
                    and bishop_unblocked(board, piece_position, next_position))
    except ValueError:
        is_valid = False
    return is_valid

def valid_king_move(board: list[str], piece: str, next_position: int) -> bool:
    try:
        piece_position = board.index(piece)
        is_valid = (square_allowed(board, piece, next_position)
                    and next_position in (piece_position - 1, piece_position + 1))
    except ValueError:
        is_valid = False
    return is_valid

def rook_unblocked(board: list[str], piece_position: int, next_position: int) -> bool:
    is_unblocked = True
    step = 1 if piece_position < next_position else -1
    initial = piece_position + 1 if piece_position < next_position else piece_position - 1
    for position in range(initial, next_position, step):
        if board[position] != ' ':
            is_unblocked = False
    return is_unblocked

def valid_rook_move(board: list[str], piece: str, next_position: int) -> bool:
    try:
        piece_position = board.index(piece)
        is_valid = (square_allowed(board, piece, next_position)
                    and rook_unblocked(board, piece_position, next_position))
    except ValueError:
        is_valid = False
    return is_valid

def valid_queen_move(board: list[str], piece: str, next_position: int) -> bool:
    return (valid_bishop_move(board, piece, next_position)
            or valid_rook_move(board, piece, next_position))

def valid_move(board: list[str], move: str) -> bool:
    if move[0].lower() in "kqrbnp" and move[1:].isdecimal() and 0 <= int(move[1:]) <= 15:
        piece = move[0]
        next_position = int(move[1:])
        if piece.lower() == 'p':
            is_valid = valid_pawn_move(board, piece, next_position)
        elif piece.lower() == 'n':
            is_valid = valid_knight_move(board, piece, next_position)
        elif piece.lower() == 'b':
            is_valid = valid_bishop_move(board, piece, next_position)
        elif piece.lower() == 'r':
            is_valid = valid_rook_move(board, piece, next_position)
        elif piece.lower() == 'k':
            is_valid = valid_king_move(board, piece, next_position)
        elif piece.lower() == 'q':
            is_valid = valid_queen_move(board, piece, next_position)
    else:
        is_valid = False
    return is_valid

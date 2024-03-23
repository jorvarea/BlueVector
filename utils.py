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

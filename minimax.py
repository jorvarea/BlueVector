from typing import Optional
from evaluation_function import evaluation_function
from valid_moves import valid_move
from utils import execute_move
from utils import is_game_finished
from config import INFINITY

def child(board: list[str], move: str) -> list[str]:
    new_board = board.copy()
    execute_move(new_board, move)
    return new_board

def generate_possible_moves(board: list[str], to_move: str) -> set[str]:
    pieces = "KQRNBP" if to_move == 'white' else "kqrnbp"
    possible_moves: set[str] = set()
    for piece in board:
        if piece in pieces:
            for position in range(16):
                if valid_move(board, f"{piece}{position}"):
                    possible_moves.add(f"{piece}{position}")
    return possible_moves

def minimax(board: list[str], depth: int, alpha: int, beta: int,
            to_move: str) -> tuple[int, Optional[str]]:
    if depth == 0 or is_game_finished(board):
        result = evaluation_function(board, depth), None
    else:
        best_move = None
        if to_move == 'white':
            max_eval = -INFINITY
            for move in generate_possible_moves(board, to_move):
                new_board = child(board, move)
                evaluation, _ = minimax(new_board, depth - 1, alpha, beta, 'black')
                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = move
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            result = max_eval, best_move
        else:
            min_eval = INFINITY
            for move in generate_possible_moves(board, to_move):
                new_board = child(board, move)
                evaluation, _ = minimax(new_board, depth - 1, alpha, beta, 'white')
                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = move
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            result = min_eval, best_move
    return result

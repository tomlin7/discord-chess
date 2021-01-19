import chess
from cogs.libs.formatter import format_content

board = chess.Board()


def legal_moves():
    return format_content(board.legal_moves)


def legal_move(move):
    return chess.Move.from_uci(move) in board.legal_moves

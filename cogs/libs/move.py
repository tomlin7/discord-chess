import chess
from cogs.libs.formatter import format_content

board = chess.Board()


def push_san(move):
    return format_content(board.push_san(move))

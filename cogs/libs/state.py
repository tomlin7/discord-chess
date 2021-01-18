import chess
from cogs.libs.formatter import format_content

board = chess.Board()


def checkmate():
    return board.is_checkmate()


def stalemate():
    return board.is_stalemate()


def insufficient_material():
    return board.is_insufficient_material()


def game_over():
    return board.is_game_over()


def draw():
    return board.can_claim_draw()

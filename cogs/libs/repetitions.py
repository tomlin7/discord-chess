import chess
from cogs.libs.formatter import format_content

board = chess.Board()


def threefold_repetition():
    return board.can_claim_threefold_repetition()


def halfmove_clock():
    return board.halfmove_clock


def fifty_moves():
    return board.can_claim_fifty_moves()


def fivefold_repetition():
    return board.is_fivefold_repetition()


def seventyfive_moves():
    return board.is_seventyfive_moves()

import chess
from cogs.libs.formatter import format_content

board = chess.Board()


def convert(value):
    values = [1, 0]
    if value not in values:
        if value.lower() == "white":
            return True
        elif value.lower() == "black":
            return False
    else:
        return value


def check():
    return board.is_check()


def attacked_by(color, square):
    return board.is_attacked_by(convert(color), chess.parse_square(square))


def attackers(color, square):
    _attackers = board.attackers(convert(color), chess.parse_square(square))
    return format_content(_attackers, "swift")


def attacker(_attacker, color, square):
    _attackers = board.attackers(convert(color), chess.parse_square(square))
    return chess.parse_square(_attacker) in _attackers

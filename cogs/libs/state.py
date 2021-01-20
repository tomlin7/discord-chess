import chess

from cogs.libs.formatter import format_content

from cogs.libs.boards import boards


def checkmate(_user_id):
    _board = boards[_user_id]
    return _board.is_checkmate()


def stalemate(_user_id):
    _board = boards[_user_id]
    return _board.is_stalemate()


def insufficient_material(_user_id):
    _board = boards[_user_id]
    return _board.is_insufficient_material()


def game_over(_user_id):
    _board = boards[_user_id]
    return _board.is_game_over()


def draw(_user_id):
    _board = boards[_user_id]
    return _board.can_claim_draw()

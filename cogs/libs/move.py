import chess

from cogs.libs.formatter import format_content

from cogs.libs.boards import boards


def push_san(_user_id, _move):
    _board = boards[_user_id]
    return format_content(_board.push_san(_move))


def undo(_user_id):
    _board = boards[_user_id]
    return _board.pop()

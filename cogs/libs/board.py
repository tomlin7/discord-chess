import chess

from cogs.libs.formatter import format_content

from cogs.libs.svg import generate_image

from cogs.libs.boards import boards


def init_board(_user_id, _value=None):
    if _value:
        _board = chess.Board(_value)
        _new_board = {
            _user_id: _board
        }
        generate_image(_board)
    else:
        _board = chess.Board()
        _new_board = {
            _user_id: _board
        }
        generate_image(_board)
    boards.update(_new_board)


def show_board(_user_id):
    _board = boards[_user_id]
    generate_image(_board)


# def fen(_user_id):
#     return format_content(board.fen())

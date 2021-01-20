from cogs.libs.boards import boards


def threefold_repetition(_user_id):
    _board = boards[_user_id]
    return _board.can_claim_threefold_repetition()


def halfmove_clock(_user_id):
    _board = boards[_user_id]
    return _board.halfmove_clock


def fifty_moves(_user_id):
    _board = boards[_user_id]
    return _board.can_claim_fifty_moves()


def fivefold_repetition(_user_id):
    _board = boards[_user_id]
    return _board.is_fivefold_repetition()


def seventyfive_moves(_user_id):
    _board = boards[_user_id]
    return _board.is_seventyfive_moves()

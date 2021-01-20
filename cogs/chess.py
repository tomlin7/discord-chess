from discord.ext import commands

from libs.data import file

from cogs.libs.board import init_board
from cogs.libs.board import show_board

from cogs.libs.moves import legal_moves
from cogs.libs.moves import legal_move

from cogs.libs.move import push_san
from cogs.libs.move import undo

from cogs.libs.state import checkmate
from cogs.libs.state import stalemate
from cogs.libs.state import insufficient_material
from cogs.libs.state import game_over
from cogs.libs.state import draw

from cogs.libs.repetitions import threefold_repetition
from cogs.libs.repetitions import halfmove_clock
from cogs.libs.repetitions import fifty_moves
from cogs.libs.repetitions import fivefold_repetition
from cogs.libs.repetitions import seventyfive_moves

from cogs.libs.attacks import check
from cogs.libs.attacks import attacked_by
from cogs.libs.attacks import attackers
from cogs.libs.attacks import attacker
from cogs.libs.attacks import attacks


class Chess(commands.Cog):
    def __init__(self, _bot):
        self.bot = _bot

    @commands.group()
    async def chess(self, _ctx):
        pass

    @chess.command()
    async def create(self, _ctx, _value=None):
        if _value:
            init_board(_ctx.author.id, _value)
        else:
            init_board(_ctx.author.id)
        await _ctx.send(file=file())

    @chess.command()
    async def board(self, _ctx):
        show_board(_ctx.author.id)
        await _ctx.send(file=file())

    @chess.command()
    async def moves(self, _ctx):
        await _ctx.send(legal_moves(_ctx.author.id))

    @chess.group(name="is")
    async def _is(self, _ctx):
        pass

    @_is.command()
    async def legal_move(self, _ctx, _move):
        await _ctx.send(legal_move(_ctx.author.id, _move))

    @chess.command()
    async def move(self, _ctx, _move):
        push_san(_ctx.author.id, _move)
        await _ctx.send(file=file())

    @chess.command()
    async def undo(self, _ctx):
        undo(_ctx.author.id)
        await _ctx.send(file=file())

    @_is.command()
    async def checkmate(self, _ctx):
        await _ctx.send(checkmate(_ctx.author.id))

    @_is.command()
    async def stalemate(self, _ctx):
        await _ctx.send(stalemate(_ctx.author.id))

    @_is.command()
    async def insufficient_material(self, _ctx):
        await _ctx.send(insufficient_material(_ctx.author.id))

    @_is.command()
    async def game_over(self, _ctx):
        await _ctx.send(game_over(_ctx.author.id))

    @_is.command()
    async def draw(self, _ctx):
        await _ctx.send(draw(_ctx.author.id))

    @_is.command()
    async def threefold_repetition(self, _ctx):
        await _ctx.send(threefold_repetition(_ctx.author.id))

    @chess.command()
    async def halfmove_clock(self, _ctx):
        await _ctx.send(halfmove_clock(_ctx.author.id))

    @_is.command()
    async def fifty_moves(self, ctx):
        await ctx.send(fifty_moves(ctx.author.id))

    @_is.command()
    async def fivefold_repetition(self, _ctx):
        await _ctx.send(fivefold_repetition(_ctx.author.id))

    @_is.command()
    async def seventyfive_moves(self, _ctx):
        await _ctx.send(seventyfive_moves(_ctx.author.id))

    @_is.command()
    async def check(self, _ctx):
        await _ctx.send(check(_ctx.author.id))

    @_is.command()
    async def attacked_by(self, _ctx, _color, _square):
        await _ctx.send(attacked_by(_ctx.author.id, _color, _square))

    @chess.command()
    async def attackers(self, _ctx, _color, _square):
        attackers(_ctx.author.id, _color, _square)
        await _ctx.send(file=file())

    @chess.command()
    async def attacks(self, _ctx, _square):
        attacks(_ctx.author.id, _square)
        await _ctx.send(file=file())

    @_is.command()
    async def attacker(self, _ctx, _attacker, _color, _square):
        await _ctx.send(attacker(_ctx.author.id, _attacker, _color, _square))


def setup(_bot):
    _bot.add_cog(Chess(_bot))

from discord.ext import commands

from cogs.libs.board import init_board
from cogs.libs.moves import legal_moves


class Chess(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def board(self, ctx):
        await ctx.send(init_board())

    @commands.command()
    async def moves(self, ctx):
        await ctx.send(legal_moves())


def setup(bot):
    bot.add_cog(Chess(bot))
